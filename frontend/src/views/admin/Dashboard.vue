<template>
    <h1>Admin Dashboard</h1>

    <h3>All users</h3>

    <div v-if="message">{{ message }}</div>

        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Role</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="user in users">
                    <td>{{ user.id }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.role }}</td>
                </tr>
            </tbody>

        </table>


</template>

<script>
import router from '@/router';

export default {
    data() {
        return {
            users: [],
            message: 'hi',
        }
    },
    methods: {
        loadUsers() {

            fetch('http://127.0.0.1:5000/users', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
            })
                .then(response => {
                    if (!response.ok) {
                        if (response.status === 401) {
                            router.push('/login');
                            throw new Error('Unauthorized: Please log in to access this resource.');
                        }
                        response.json().then(data => {
                            this.message = data.message || 'Error occurred';
                        });
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    this.users = data.users;
                    this.message = data.message;
                })
                .catch(error => {
                    console.error('Error fetching message:', error);
                    this.message = 'Error fetching message';
                });
        }
    },
    mounted() {
        this.loadUsers();
    },
}

</script>

<style scoped>

    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }

    th, td {
    padding: 8px;
    text-align: left;
    }

</style>