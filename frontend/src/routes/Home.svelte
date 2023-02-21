<!-- connect frontend backend  -->
<script>
    import fastapi from "../lib/api";
    import { link } from 'svelte-spa-router'
    let question_list = []
  //빈 배열 만들고 데이터 조회하여 얻은 데이터 변수에 넣고 호출하기
  function get_question_list() {
    fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json
        })
  }
  
  get_question_list()
  </script>
  <ul>
    {#each question_list as question}
      <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
  </ul>
  <!-- use:link로 ur에 해시 # 를 사용하는 이유는 
해시 뒤에 오는 게 어떤 페이지이던 브라우저가 동일한 페이지로 인식하게 하여 프론트단에만 사용하는 페이지를 만들어 서버 에러가 나지 않도록 함  -->