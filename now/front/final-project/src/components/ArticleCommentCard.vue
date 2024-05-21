<template>
  <div style="border: 2px solid black;">
    <p> 대상 : {{ comment.title }}</p>
    <p> 의견 : {{ comment.content }}</p>
    <p> 분류 : {{ comment.category }}</p>
    <p> 생성 시간 : {{ comment.created_at }}</p>
    <p> 수정 시간 : {{ comment.updated_at }}</p>

  </div>
</template>

<script setup>

defineProps({
  comment : Object
})


</script>

<style scoped>

</style>