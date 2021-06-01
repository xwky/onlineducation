// 注册
export const addSignUpUser = ({ commit }, data) => {
    return new Promise((resolve, reject) => {
     

      
    });
  };

// 登录
export const login = ({ commit},data) => {
    return new Promise((resolve,reject) => {
        // if (data.username === '15039715531' && data.password === '123456'){
        //     localStorage.setItem('loginInfo',JSON.stringify(data));
        //     commit('SET_USER_LOGIN_INFO',data);
        //     resolve(true);
        //     return true;
        // }
        const userArr = localStorage.getItem('users');
        let users = [];
      if (userArr) {
        users = JSON.parse(userArr);
      }
      users.push(data);
      localStorage.setItem('users', JSON.stringify(users));
        // const userArr = localStorage.getItem('users');
        // console.log('6',userArr);
        if (userArr){
            const users = JSON.parse(userArr);
            for (const item of users){
                if (item.username === data.username && item.password === data.password){
                    localStorage.setItem('loginInfo',JSON.stringify(item));
                    commit('SET_USER_LOGIN_INFO',item);
                    resolve(true);
                    break;
                }
            }
        } else{
            resolve(false);
        }
    });
};

// 判断是否登录
export const isLogin = ({commit}) => {
    const user = localStorage.getItem('loginInfo');
    if (user){
        commit('SET_USER_LOGIN_INFO',JSON.parse(user));
    }
};

// 退出登录
export const signOut = ({commit}) => {
    localStorage.removeItem('loginInfo');
    commit('SET_USER_LOGIN_INFO',{})
    localStorage.setItem('userid','')
}