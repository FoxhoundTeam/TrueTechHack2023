<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-sheet
          class="pa-12 mx-auto"
          max-width="500"
          color="grey lighten-3"
          rounded
          elevation="1"
        >

          <v-text-field
            v-model="username"
            label='Логин'
            outlined
            clearable
            background-color="white"
            :rules="[rules.required]" 
          ></v-text-field>

          <v-text-field
            v-model="password"
            label='Пароль'
            outlined
            clearable
            background-color="white"
            :rules="[rules.required]" 
            :type="show1 ? 'text' : 'password'"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show1 = !show1"
          ></v-text-field>

          <v-btn
            depressed
            color="primary"
            rounded
            dark
            large
            @click="login"
          >
            Вход
          </v-btn>

        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src

// import { stringify } from 'querystring';

export default {
  name: 'LoginView',
  data(){
    return {
      list_model: Array(50).fill("x"),//["элемент"]*100;
      username: '',
      password: '',
      show1:false,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        emailMatch: () => (`The email and password you entered don't match`),
      },
    }
  },

  methods:{
    login(){},
  },

  beforeCreate(){},

  created() {},

  beforeMount(){},

  mounted() {},

  computed: {},

  watch: {},
}
</script>
