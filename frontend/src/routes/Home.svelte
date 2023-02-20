<!-- connect frontend backend  -->
<script>
    import fastapi from "../lib/api";
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
      <li>{question.subject}</li>
    {/each}
  </ul>