<template>
<!-- 
    title = models.CharField(max_length=100)
    content = models.TextField(null = False)
    category = models.TextField()
 -->
  <div>
    {{ movie.title }}
    <img class="img" :src=imgUrl alt="X">
  </div>

  <div class="mb-3">
    <label for="category" class="form-label"></label>
    <select v-model="comment.category" class="form-select" style="width: auto">
      <option v-for="n in category" :key="n" :value="n">{{ n }}</option>
    </select>
  </div>

  <div class="mb-3">
    <label for="title" class="form-label">{{ comment.category }}</label>
    <input type="text" class="form-control" id="title" placeholder="이야기하고 싶은 ~~을 적어주세요." v-model="comment.title" required />
  </div>
  <div class="mb-3">
    <label for="content" class="form-label">의견</label>
    <textarea class="form-control" v-model="comment.content" placeholder="내 의견은..." rows="5" required></textarea>
  </div>
  <button @click="submitComment" class="btn btn-info mb-5">제출</button>
  <!-- 아티클카드로 정보 보내서 DB에 저장된 comments 정보들 v-for로 전송해서 띄우기 -->
  <ArticleCommentCard v-for="comment in comments" :key="comment.pk" :comment="comment"/>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {ref, watch} from 'vue'
import { useCounterStore } from '@/stores/counter'
import ArticleCommentCard from '@/components/ArticleCommentCard.vue';
import axios from "axios"

const store = useCounterStore()
const movie = ref({})
const route = useRoute()
movie.value = {
  'title': route.query.title,
  'poster_path' : route.query.poster_path
}
const imgUrl = "https://image.tmdb.org/t/p/original" + movie.value.poster_path


const movieId = route.params.movieId

const category = [
  '대사',
  '장면',
  '인물',
  '사물',
  '소리',
  '기타',
]
const comment = ref({
  category:'분류',
  title:'',
  content:''
})

const comments = ref([])
axios ({
  method : 'get',
  url : `http://127.0.0.1:8000/movies/${movieId}/community/`
}).then((response) =>{
  comments.value = response.data
  console.log(response.data)
}).catch((error) =>{
  console.log(error)
})

const submitComment = () => {
  console.log('제출')
  store.addComment(movieId, comment.value)
  .then((response) => {
    axios ({
      method : 'get',
      url : `http://127.0.0.1:8000/movies/${movieId}/community/`
    }).then((response) =>{
      comments.value = response.data
      console.log(response.data)
    }).catch((error) =>{
      console.log(error)
    })
    comment.value = {
      category : '분류',
      title : '',
      content : ''
    }
  }).catch((error) => {
    console.log(error)
  })

}
// watch(comments, (Newcomments)=>{
//   comments.value = Newcomments
//   axios ({
//   method : 'get',
//   url : `http://127.0.0.1:8000/movies/${movieId}/community/`
// }).then((response) =>{
//   comments.value = response.data
//   console.log(response.data)
// }).catch((error) =>{
//   console.log(error)
// })
// })


</script>
<style scoped>

*{
  color : white
}
.img {
  width : 20rem;
  height: 30rem;
}
</style>
