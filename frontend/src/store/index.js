import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: null,
        username: null,
        current_user:null,
        // app: null,
        // error_show: false,
        // error_string: "",
        // searchstring: "",
        // selected_language:"en",
    },
    getters: {
        getToken(state) {
            return state.token;
        },
        getUsername(state) {
            return state.username;
        },
        // getSearchstring(state) {
        //     return state.searchstring;
        // },
        // getSelectedLanguage(state) {
        //     return state.selected_language;
        // },
        getCurrentUser(state){
            return state.current_user;
        },
    },
    mutations: {
        initialiseStore(state) {
            // извлечение полей vuex из localStorage для хранения данных
            // между перезагрузками страницы

            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token');
            }
            if (localStorage.getItem('username')) {
                state.username = localStorage.getItem('username');
            }
            // if (localStorage.getItem('searchstring')) {
            //     state.searchstring = localStorage.getItem('searchstring');
            // }
            if (localStorage.getItem('current_user')) {
                state.current_user = JSON.parse(localStorage.getItem('current_user')); // объекты нужно десериализовать из localstorage
            }
        },

        // набор сет-методов для сохранения полей vuex в localstorage
        // для сохранности данных после перезагрузки страницы
        setToken(state, data) {
            state.token = data;
            localStorage.setItem("token", data); // простые типы можно сохранять через setItem

        },
        setUsername(state, data) {
            state.username = data;
            localStorage.setItem("username", data); // простые типы можно сохранять через setItem
        },
        // setSearchstring(state, data){
        //     state.searchstring = data;
        //     localStorage.setItem("searchstring", data); // простые типы можно сохранять через setItem
        // },
        // setSelectedLanguage(state, data) {
        //     state.selected_language = data;
        //     localStorage.setItem("selected_language", data); // простые типы можно сохранять в localStorage через setItem
        // },
        setCurrentUser(state, data){
            // state.current_user = data;
            state.current_user = data;
            localStorage.setItem("current_user", JSON.stringify(data)); // объекты нужно сериализовать в localStorage
        }
    },
    actions: {

    },
    modules: {

    }
})