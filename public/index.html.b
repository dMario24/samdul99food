<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>삼둘푸드</title>
</head>
<body>
    <h1>음식 이름 입력</h1>
    <form id="foodForm">
        <label for="foodName">음식 이름: </label>
        <input type="text" id="foodName" name="foodName" required>
        <button type="submit">저장</button>
    </form>

    <script>
        document.getElementById("foodForm").addEventListener("submit", function(event) {
            event.preventDefault(); // 폼 기본 제출 방지

            const foodName = document.getElementById("foodName").value;
            const url = `http://ec2-43-203-204-195.ap-northeast-2.compute.amazonaws.com/n77/food?name=${encodeURIComponent(foodName)}`;

            fetch(url, {
                method: 'GET',
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>

    <script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyCaq--eTrpf_f29baw_NhJoGnhmEyWTEDc",
    authDomain: "samdul77food.firebaseapp.com",
    projectId: "samdul77food",
    storageBucket: "samdul77food.appspot.com",
    messagingSenderId: "837529612336",
    appId: "1:837529612336:web:143e6e91d6bb2d98023df5",
    measurementId: "G-D3G5893TD0"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>
</body>
</html>
