<template>
  <div>
    <div class="page">
      <div class="signup">
        <h3>Let's create a new account!</h3>
        <form action="">
          <input class="form-background" type="text" placeholder="Email" v-model="email"><br>
          <input class="form-background" type="password" placeholder="Password" v-model="password"><br>
          <div id="terms">
            <input type="checkbox" id="checkbox" v-model="agreed">
            <label for="checkbox">By signing up you agree to our <router-link to="/terms">general business terms.</router-link></label>
          </div>
        </form>
        <button class="button-special" @click="signUp">Sign up!</button>
        <p id="status">{{status}}</p>
        <p> <router-link to="/login">or login...</router-link> </p>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase'
export default {
  name: 'signup',
  data () {
    return {
      email: '',
      password: '',
      status: '',
      resend: false,
      agreed: false
    }
  },
  methods: {
    signUp: function () {
      if (this.agreed) {
        firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then(
          () => {
            const user = firebase.auth().currentUser
            if (user.emailVerified === true) {
              this.$router.replace('dashboard')
            } else {
              // Send verification email
              user.sendEmailVerification()
              this.status = 'Please check your email to activate your account.'
              // TODO SEND PROP
              this.$router.replace('verify')
            }
          },
          (err) => {
            this.status = err.message
          })
      } else {
        this.status = 'You need to accept our terms.'
      }
    }
  },
  watch: {
    email: function () {
      this.email = this.email.trim()
    }
  }
}
</script>

<style scoped>
#checkbox {
width: auto !important}
.signup {
  text-align: center;
  margin-top: 40px;
}
.social-button {
  width: 75px;
  padding: 10px;
  background: white;
  border-radius: 100%;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2);
  outline: 0;
  border: 0;
}

.social-button:active {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
}

.social-button img {
  width: 100%
}

input {
    margin: 10px 0;
    width: 30%;
    padding: 15px;
}
@media (max-width: 800px) {
  input {
    width: 70% !important;
  }
}
button {
    margin-top: 20px;
    cursor: pointer;
}

p {
margin-top: 40px;
font-size: 13px;
}
p a {
    text-decoration: underline;
    cursor: pointer;
}
#status {
  color: red;
}
#terms {
  font-size: 14px;
  color: darkgray;
}
#terms  a:link {
  color: gray;
  text-decoration-line: none !important;
}
/* visited link */
#terms a:visited {
  color: gray;
}
/* mouse over link */
#terms a:hover {
  color: #ff322e;
}
.page {
  padding-bottom: 400px;
}
</style>
