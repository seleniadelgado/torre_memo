console.log('hello')
const hello = () => {
    const memoText = document.getElementById("memo-text").value;
    data = {'memo': memoText};
    $().({
        type: "POST",
        url: `/memos/api/memos/${memo_id}`,
        data: data,
      });
}
const memo = document.getElementById('save-memo-btn')
memo.addEventListener('click', hello)