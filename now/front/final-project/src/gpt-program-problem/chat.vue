<template>
  <div>
    <!-- 채팅창 화면 -->
    <section class="container section-scrollable" style="margin-top:5rem">
      <!-- 프로필 영역 -->
      <div class="top-area">
        <div class="profile-area">
          <span class="dokdo-regular" style="margin-top:50px ;">길라잡이</span>
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
      const answer ="길라잡이"
      this.addChat("receive", answer);
    },
    sendMessageToServer(message) {
      const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions';
      const API_KEY = import.meta.env.VITE_GPT_API_KEY;
      const headers = {
        Authorization: `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      };
      const data = {
        model: 'gpt-4o',
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
.section-scrollable{
  height: 80vh;
  overflow-y: auto;
}
.dokdo-regular {
  font-family: "Dokdo", system-ui;
  font-weight: 400;
  font-style: normal;
  font-size:6vh;
  color: #3f4040;
  text-align: center;
}
</style>
