<template>
    <h1>Create account to dive in</h1>

    <form action="">
        <input type="text" placeholder="Username" />
        <input type="password" placeholder="Password" />
        <input type="password" placeholder="Confirm Password" />
        <button type="submit">Register</button>
    </form>

    <div id="msg"></div>
    <button @click="showMessage">Show Message</button>

</template>

<script setup>

function showMessage() {
    const msg = document.getElementById('msg');
    fetch('http://127.0.0.1:5000')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            msg.innerText = data.message;
        })
        .catch(error => {
            console.error('Error fetching message:', error);
            msg.innerText = 'Error fetching message';
        });
}

</script>