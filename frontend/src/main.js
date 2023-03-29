import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'

Vue.config.productionTip = false

const token = localStorage.getItem('token');
if (token) {
    Vue.prototype.$http.defaults.headers.common['Authorization'] = 'Token ' + token;
}

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.state.token) {
            next({
                name: 'LoginView',
                //query: { redirect: to.fullPath }
            });
        } else {
            next();
        }
    } else {
        next();
    }
});

new Vue({
  vuetify,
  router,
  store,
  beforeCreate() {
    this.$store.commit('initialiseStore');
  },
  render: h => h(App)
}).$mount('#app')
