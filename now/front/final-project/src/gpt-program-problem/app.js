// 채팅 전송 및 수신을 위한 선택
const chatInput = document.querySelector('.chat-input')
const chatContainer = document.querySelector('.chat-area')

// 채팅창에 내용을 추가해주는 부분
const addChat = (type, value) => {
  const chat = document.createElement('div')
  chat.classList.add('chat')
  chat.innerText = value
  chat.classList.add(`${type}-chat`)
  chatContainer.appendChild(chat)
  chatContainer.scrollTop = chatContainer.scrollHeight
}

// 1. 챗봇 서버에 요청할 URL (chatGPT API reference Chat 파트 참고)
const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions'

// 2. API 키 (발급 받은 Secret Key)
const API_KEY ='sk-proj-2y5MeZ5AwEShg3zqkkbET3BlbkFJMURTlOkcUQlACUtQ8OdU'

// 필요한 헤더 정보
const headers = {
  Authorization: `Bearer ${API_KEY}`, // 인증 키 설정
  'Content-Type': 'application/json' // 요청 데이터의 타입
}

// 이전에 응답받은 메세지를 저장하는 변수
let oldMsg = ''

const chatReceive = (userMsg) => {
  const data = {
    model: 'gpt-3.5-turbo',
    messages: [
      { role: 'user', content: userMsg },
      { role: 'system', content: oldMsg }
    ]
  };

  // 서버에 요청을 보내고 응답을 처리하는 부분
  axios.post(OPEN_API_URL, data, { headers })
    .then(response => {
      const answer = response.data.choices[0].message.content;
      addChat('receive', answer); // 서버 응답을 채팅창에 추가
      oldMsg = answer; // 이전 메시지 업데이트
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

const chatSubmit = () => {
  const value = chatInput.value.trim(); // 입력 값 앞뒤 공백 제거
  if (!value) return;

  addChat('send', value); // 사용자가 보낸 채팅 표시

  // 서버에 메시지 전송
  chatReceive(value);

  chatInput.value = ''; // 입력창 초기화
}

chatInput.addEventListener('keyup', (e) => {
  e.key === 'Enter' && chatSubmit()
})
