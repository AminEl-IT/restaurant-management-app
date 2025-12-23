<template>
    <HeaderView />
    <h1>Hello {{ name }}, Welcome on Update Restaurant Page</h1>
    <div class="form-container">
        <form class="restaurant-form" @submit.prevent="updateRestaurant">
            <h2>Update Restaurant</h2>

            <input type="text" placeholder="Restaurant Name" v-model="restaurant.name" required />

            <input type="text" placeholder="Contact Number" v-model="restaurant.contact" required />

            <input type="text" placeholder="Address" v-model="restaurant.address" required />

            <button type="submit">Update Restaurant</button>
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
                name: '',
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
        async updateRestaurant() {
            await axios.put(
                'http://localhost:8000/api/restaurants/' + this.$route.params.id + '/',
                {
                    name: this.restaurant.name,
                    address: this.restaurant.address,
                    contact: this.restaurant.contact
                }
            )

            alert('Restaurant updated successfully')
            this.$router.push('/')
        }

    },
    async mounted() {
        let user = localStorage.getItem('user-info');
        this.name = JSON.parse(user).name;
        if (!user) {
            this.$router.push({ name: 'SignUp' })
        }

        const result = await axios.get('http://localhost:8000/api/restaurants/' + this.$route.params.id + '/')
        this.restaurant = result.data
    }
}
</script>