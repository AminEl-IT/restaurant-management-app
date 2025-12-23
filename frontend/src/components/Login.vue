<template>
    <img class="logo" src="../assets/resto-amin.png">

    <div class="container">
        <form class="login" @submit.prevent="login">
            <h2>Login</h2>

            <input type="email" v-model="email" placeholder="Enter Email" required>

            <input type="password" v-model="password" placeholder="Enter Password" required>

            <button type="submit">Login</button>

            <p class="login-link">
                Don’t have an account?
                <router-link to="/signup">Sign up</router-link>
            </p>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default
    {
        name: 'LoginView',
        data() {
            return {
                email: '',
                password: ''
            }
        },
        methods:
        {
            async login() {
                try {
                    const result = await axios.post(
                        'http://localhost:8000/api/auth/login/',
                        {
                            email: this.email,
                            password: this.password
                        }
                    )

                    localStorage.setItem('user-info', JSON.stringify(result.data))
                    this.$router.push('/')

                } catch (error) {
                    alert('Invalid email or password')
                }
            }
        },

        mounted() {
            let user = localStorage.getItem('user-info');
            if (user) {
                this.$router.push({ name: 'HomeView' })
            }
        }
    }
</script>