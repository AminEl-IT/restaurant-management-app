<template>
    <HeaderView />
    <h1>Hello {{ name }}, Welcome on Add Restaurant Page</h1>
    <div class="form-container">
        <form class="restaurant-form" @submit.prevent="addRestaurant">
            <h2>Add Restaurant</h2>

            <input type="text" placeholder="Restaurant Name" v-model="restaurant.namerest" required />

            <input type="text" placeholder="Contact Number" v-model="restaurant.contact" required />

            <input type="text" placeholder="Address" v-model="restaurant.address" required />

            <button type="submit">Add</button>
        </form>
    </div>
</template>

<script>
import HeaderView from './Header.vue';
import axios from 'axios';
export default {
    name: 'HomeView',
    data() {
        return {
            name: '',
            restaurant: {
                namerest: '',
                address: '',
                contact: ''
            }
        }
    },
    components: {
        HeaderView
    },
    methods:
    {
        async addRestaurant() {
            if (!this.restaurant.namerest || !this.restaurant.address || !this.restaurant.contact) {
                alert('Please fill all fields')
                return
            }

            await axios.post('http://localhost:8000/api/restaurants/', {
                name: this.restaurant.namerest,
                address: this.restaurant.address,
                contact: this.restaurant.contact
            })

            alert('Restaurant added successfully')

            this.$router.push('/')
        }
    },
    mounted() {
        let user = localStorage.getItem('user-info');
        this.name = JSON.parse(user).name;
        if (!user) {
            this.$router.push({ name: 'SignUp' })
        }
    }
}
</script>

<style>
.form-container {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}

.restaurant-form {
    width: 350px;
    background: #ffffff;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.restaurant-form h2 {
    text-align: center;
    color: #333;
    margin-bottom: 10px;
}

.restaurant-form input {
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ddd;
    font-size: 14px;
    transition: 0.3s ease;
}

.restaurant-form input:focus {
    outline: none;
    border-color: #ff914d;
    box-shadow: 0 0 6px rgba(255, 145, 77, 0.4);
}

.restaurant-form button {
    padding: 12px;
    border: none;
    border-radius: 8px;
    background: linear-gradient(135deg, #ff914d, #4caf50);
    color: white;
    font-size: 16px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s ease;
}

.restaurant-form button:hover {
    opacity: 0.9;
}
</style>