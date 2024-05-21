<template>
  <div style="border: 2px solid black;">
    <p> 대상 : {{ comment.title }}</p>
    <p> 의견 : {{ comment.content }}</p>
    <p> 분류 : {{ comment.category }}</p>
    <p> 생성 시간 : {{ formattedDate }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'
const props = defineProps({
  comment : Object
})
const formattedDate = computed(() => {
  let date = new Date(props.comment.created_at)
  let year = date.getFullYear()
  let month = ('0' + (date.getMonth() + 1)).slice(-2)
  let day = ('0' + date.getDate()).slice(-2)
  let hours = ('0' + date.getHours()).slice(-2)
  let minutes = ('0' + date.getMinutes()).slice(-2)
  return `${year}-${month}-${day} ${hours}:${minutes}`
})
</script>

<style scoped>

</style>