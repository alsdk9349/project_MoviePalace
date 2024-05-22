<template>
  <div>
    <!-- 채팅창 화면 -->
    <section class="container section-scrollable" style="margin-top:5rem">
      <!-- 프로필 영역 -->

          <div class="top-area">
            <div class="profile-area">
              <span >길라잡이</span>
            </div>
          </div>
          <!-- 채팅 영역 -->
          <div class="chat-area" ref="chatArea"></div>
          
          <!-- 채팅창 하단 영역 -->
          <div class="bottom-area">
            <input class="chat-input" type="text" placeholder="할말을 입력해주세요" ref="chatInput" />
          </div>
      </section>
  </div>
</template>

<script>
import axios from 'axios';
import {ref} from 'vue';
export default {
  mounted() {
    this.$nextTick(() => {
      const chatInput = this.$refs.chatInput;
      chatInput.addEventListener('keyup', this.chatSubmit);
    });
  },
  methods: {
    chatSubmit(event) {
      if (event.key === 'Enter') {
        const value = event.target.value.trim();
        if (!value) return;
        this.addChat('send', value);
        this.chatReceive(value);
        this.sendMessageToServer(value); // 새로운 메서드 추가
        event.target.value = '';
      }
    },
    addChat(type, value) {
      const chatContainer = this.$refs.chatArea;
      const chat = document.createElement('div');
      chat.classList.add('chat');
      chat.innerText = value;
      chat.classList.add(`${type}-chat`);
      chatContainer.appendChild(chat);
      chatContainer.scrollTop = chatContainer.scrollHeight;
    },
    chatReceive(userMsg) {
      // const answer = ref("");
      // this.addChat("receive", answer.value);
      const answer ="길라잡이"
      this.addChat("receive", answer);
    },
    sendMessageToServer(message) {
      const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions';
      const API_KEY = 'sk-proj-2y5MeZ5AwEShg3zqkkbET3BlbkFJMURTlOkcUQlACUtQ8OdU';
      const headers = {
        Authorization: `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      };
      const data = {
        model: 'gpt-3.5-turbo',
        messages: [
          { role: 'user', content: message },
          { role: 'system', content: this.oldMsg }
        ]
      };
      axios.post(OPEN_API_URL, data, { headers })
        .then(response => {
          const answer = response.data.choices[0].message.content;
          this.addChat('receive', answer);
          this.oldMsg = answer;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  },
  data() {
    return {
      oldMsg: ''
    };
  }
};

import './style.css'
</script>

<style scoped>
/* .send-chat {
  
  background-color: black;
  align-self: flex-end;
  color : white;
} */

/* .receive-chat {
  background-color: var(--color-gray);
} */
.section-scrollable{
  height: 80vh;
  overflow-y: auto;
}

</style>
