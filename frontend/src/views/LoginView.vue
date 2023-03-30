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

// eslint-disable-next-line no-unused-vars
import axios from 'axios'

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
    login(){
        // this.$store.commit('setToken', "123456789");
        // this.$store.commit('setUsername', "Пользователь");
        // this.$router.replace({name:"MainView"});
        // return; //TODO временно
        
        axios.post("/api/auth",
                  { username:this.username,
                    password:this.password } )
          .then(response => {
            //console.log("response.data = ", response.data);
            const tmp_token = response.data.token;
            if(tmp_token && tmp_token.length==40){
              this.$store.commit('setToken', tmp_token);
              this.$store.commit('setUsername', this.username);
              axios.defaults.headers.common['Authorization'] = "Token "+ tmp_token;
              console.log(localStorage);
              this.$router.replace({name:"MainView"});
              // axios.get("/api/staff",{params:{id:"current"}})
              // .then(response => {
              //   this.$store.commit('setCurrentUser', response.data.staff);
              //   // TODO в зависимости от группы показать элементы интерфейса
              //   console.log("this.$store.state.current_user = ", this.$store.state.current_user);
              //   this.$router.replace({name:"MainView"});
              // })
              // .catch(error => {
              //   this.$emit('showerror', error);
              // })
              
            }
            else{
              this.$emit('showerror', "Неверный логин или пароль");
            }
          })
          .catch(error => {
            this.$emit('showerror', error);
          });
          
      }
  },


  beforeMount () {
    // console.log("beforeMount Token=",this.$store.state.token); // I'm text inside the component.
    if(this.$store.state.token && this.$store.state.username){
      this.$router.replace({name:"MainView"});
    }
  },

  mounted() {},

  computed: {},

  watch: {},
}
</script>
