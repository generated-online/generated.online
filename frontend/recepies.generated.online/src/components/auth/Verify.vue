<template>
<div class>
  <div class="content content-wrap">
    <div class="verify">
      <h3>Please verify your email!</h3>
      <hr>
      <p>Make sure to check your spam folder.</p>
      <p id="status">{{status}}</p>
      <p> <router-link to="/login">Go to login page.</router-link> </p>
      <br>
      <p>If you have not recieved an email:</p>
      <button @click="verifyAgain" class="button">Send verification email again</button>
    </div>
  </div>
</div>
</template>

<script>
import firebase from 'firebase'
    export default {
        name:  'verify',
        data() {
            return {
              status: '',
            };
        },
        methods: {
          verifyAgain: function() {

            const user = firebase.auth().currentUser;

            // Send verification email
            user.sendEmailVerification();
            self.status = 'Please check your email to activate your account.'
          }
        }
    }
</script>

<style scoped>
input {
    margin: 10px 0;
    width: 30%;
    padding: 15px;
}

.content {
  text-align: center;
}

#status {
  color: red;
}
</style>
