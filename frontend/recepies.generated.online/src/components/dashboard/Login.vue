<template>
    <v-container>
        <v-card dark>
            <v-card-title>Login</v-card-title>
            <v-card-text>
                <v-alert v-if="error"
                         color="red"
                         dense
                         dismissible
                         outlined
                         type="error">{{ error }}
                </v-alert>
                <v-form @submit.prevent="submit">
                    <v-text-field v-model="form.email"
                                  autofocus
                                  label="E-Mail"
                                  required
                                  style="width: 100%">

                    </v-text-field>
                    <v-text-field
                            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                            :type="showPassword ? 'text' : 'password'"
                            name="input-10-2"
                            label="Password"
                            v-model="form.password"
                            required
                            class="input-group--focused"
                            @click:append="showPassword = !showPassword"
                    ></v-text-field>
                    <v-btn
                            color="success"
                            class="mr-4"
                            @click="submit"
                    >
                        Login
                    </v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
import firebase from "firebase";

export default {
    data() {
        return {
            form: {
                email: "",
                password: ""
            },
            error: null,
            showPassword: false,
        };
    },
    created() {
        this.$emit('recipe', null);
    },
    methods: {
        submit() {
            firebase
                .auth()
                .signInWithEmailAndPassword(this.form.email, this.form.password)
                .then(data => {
                    this.$router.replace("/dashboard");
                })
                .catch(err => {
                    this.error = err.message;
                });
        }
    }
};
</script>