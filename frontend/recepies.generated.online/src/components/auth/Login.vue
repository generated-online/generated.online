<template>
  <div class="light-background">
    <div class="login">
      <h3>Log In</h3>
      <form>
      <input class="form-background" type="text" placeholder="Email" v-model="email"><br>
      <input class="form-background" type="password" placeholder="Password" v-model="password"><br>
      </form>
      <button class="button-special" @click="login">Log In</button>

      <!-- <p>
        or sign in with Google <br>
        <button @click="googleLogin" class="social-button">
          <img src="../assets/google-favicon.svg" alt="Google Logo">
        </button>
      </p> -->

      <p id="status">{{status}}</p>

      <button v-if="resend" @click="resendEmail" class="button">Resend e-mail.</button>
      <p>
        <span class="reset">
          Forgot your password? <a @click="sendResetEmail">Send reset e-mail.</a>
        </span>
        <br>
        <span>
          You don't have an account? <router-link to="/signup">Create one!</router-link>
        </span>
      </p>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase'

export default {
  name: 'login',
  data () {
    return {
      email: '',
      password: '',
      status: '',
      resend: false
    }
  },
  methods: {
    login: function () {
      firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
        () => {
          if (firebase.auth().currentUser.emailVerified) {
            this.$router.replace('dashboard')
          } else {
            this.status = 'Please confirm your e-mail!';
            this.resend = true
          }
        },
        (err) => {
          this.status = err.message
        }
      )
    },
    resendEmail: function () {
      firebase.auth().currentUser.sendEmailVerification();
      this.status = 'We have re-sent you a verification email. Please check your spam folder as well.';
      this.resend = false
    },
    sendResetEmail: function () {
      if (this.email === '') {
        this.status = 'Please enter your email in the field above.'
      } else {
        firebase.auth().sendPasswordResetEmail(this.email).then(
          () => { this.status = 'An email was sent to you it the account exists.' }, () => this.status = 'Please enter your email in the field. It must be correctly formatted.')
      }
    },
    googleLogin: function () {
      // Using a popup.
      var provider = new firebase.auth.GoogleAuthProvider();
      provider.addScope('profile');
      provider.addScope('email');
      firebase.auth().signInWithPopup(provider).then((result) => {
        this.$router.replace('dashboard')
      }).catch((err) => {
        this.status = err.message
      })
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
.login {
  text-align: center;
  margin-top: 40px;
  padding-bottom: 400px;
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

.reset {
  color: darkgrey;
}
.reset:hover a {
  color: red;
}

#status {
  color: #ff322e;
}
</style>
