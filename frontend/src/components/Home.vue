<template>
    <HeaderView />
    <h1>Hello {{ name }}, Welcome on Home Page</h1>
    <table class="restaurant-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Address</th>
                <th>Contact</th>
                <th class="th-actions"></th>
            </tr>
        </thead>

        <tbody>
            <tr v-for="item in restaurant" :key="item.id">
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.address }}</td>
                <td>{{ item.contact }}</td>
                <td class="actions">
                    <router-link :to="'/update/' + item.id" class="btn-update">
                        Update
                    </router-link>

                    <button class="btn-delete" @click="deleteRestaurant(item.id)">
                        Delete
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import HeaderView from './Header.vue';
import axios from 'axios';
export default {
    name: 'HomeView',
    data() {
        return {
            name: '',
            restaurant: []
        }
    },
    methods:
    {
        async deleteRestaurant(id) {
            const confirmed = confirm("Are you sure you want to delete this restaurant?");

            if (!confirmed) {
                return;
            }

            let result = await axios.delete(
                "http://localhost:8000/api/restaurants/" + id + "/"
            );

            if (result.status === 204 || result.status === 200) {
                this.loadData();
            }
        },
        async loadData() {
            let user = localStorage.getItem('user-info');

            if (!user) {
                this.$router.push({ name: 'SignUp' })
                return
            }

            this.name = JSON.parse(user).name;

            let result = await axios.get("http://localhost:8000/api/restaurants/")
            this.restaurant = result.data;
        }
    },
    components: {
        HeaderView
    },
    async mounted() {
        this.loadData();
    }
}
</script>

<style>
.restaurant-table {
    width: 90%;
    margin: 30px auto;
    border-collapse: collapse;
    background-color: white;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    overflow: hidden;
}

.restaurant-table th,
.restaurant-table td {
    padding: 14px 16px;
    text-align: left;
}

.restaurant-table thead {
    background: linear-gradient(135deg, #ff914d, #4caf50);
    color: white;
}

.restaurant-table tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

.restaurant-table tbody tr:hover {
    background-color: #f1f1f1;
}

.restaurant-table th {
    font-weight: bold;
    text-transform: uppercase;
    font-size: 13px;
}

.actions {
    display: flex;
    gap: 10px;
}

.btn-delete {
    padding: 6px 12px;
    border: none;
    border-radius: 6px;
    background-color: #e74c3c;
    color: white;
    font-size: 14px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.2s ease;
}

.btn-delete:hover {
    background-color: #c0392b;
}

.btn-delete:active {
    transform: scale(0.97);
}

.actions {
    display: flex;
    gap: 10px;
}

.btn-update {
    padding: 6px 12px;
    border-radius: 6px;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    font-size: 14px;
    font-weight: bold;
    transition: 0.2s ease;
}

.btn-update:hover {
    background-color: #2980b9;
}

.btn-update:active {
    transform: scale(0.97);
}

.th-actions {
    width: 180px;
    text-align: center;
}

.actions {
    width: 180px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}
</style>