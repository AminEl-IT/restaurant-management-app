<template>
    <img class="logo" src="../assets/resto-amin.png">
    <div class="container">
        <form action="Signup" class="register" @submit.prevent="signUp">
            <h2>Create Account</h2>

            <input type="text" v-model="name" placeholder="Enter Name" required>
            <input type="email" v-model="email" placeholder="Enter Email" required>
            <input type="password" v-model="password" placeholder="Enter Password" required>

            <button type="submit">Register</button>

            <p class="login-link">
                Already have an account?
                <router-link to="/login">Login</router-link>
            </p>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',

    data() {
        return {
            name: '',
            email: '',
            password: ''
        }
    },

    methods: {
        //set api, localstorage, router vers home
        async signUp() {
            try {
                const result = await axios.post(
                    'http://localhost:8000/api/auth/register/',
                    {
                        name: this.name,
                        email: this.email,
                        password: this.password
                    }
                )

                console.log(result.data)

                localStorage.setItem(
                    'user-info',
                    JSON.stringify(result.data)
                )

                this.$router.push({ name: 'HomeView' })

            } catch (error) {
                console.error(error)
                alert('Error during signup')
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


<style></style>