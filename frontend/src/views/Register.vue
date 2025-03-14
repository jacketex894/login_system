<template>
    <div>
        <h2> Register </h2>
        <div>
            <label> Account </label>
            <input v-model="account"/>
        </div>
        <div>
            <label> Email Address </label>
            <input v-model="email"/>
        </div> 
        <div>
            <label> Password </label>
            <input v-model="password"/>
        </div> 
    </div>
    <button v-on:click="show()"> Login </button>
</template>
<script>

export default {
    name: 'Register',
    data(){
        return{
            account:null,
            email:null,
            password:null,
        };
    },
    methods:{
        show(){
            console.log(this.account)
            console.log(this.email)
            console.log(this.password)
        }
    }
}
</script>