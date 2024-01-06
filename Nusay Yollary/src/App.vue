
<script setup>
import axios from 'axios';
import {RouterView, useRouter} from "vue-router"
import {ref, onMounted} from 'vue'
import {useI18n}  from "vue-i18n"
import i18n from './plugins/i18n'
import Cookies from 'js-cookie'
import CommunityIcon from './components/icons/IconCommunity.vue'
import IconTooling from "./components/icons/IconTooling.vue"
import IconSupport from "./components/icons/IconSupport.vue"
import IconEcosystem from "./components/icons/IconEcosystem.vue"
import Search from './components/Search.vue';
// import func from "../vue-temp/vue-editor-bridge"




const  usei18n  = useI18n()
if(localStorage.lang){
  usei18n.locale.value = localStorage.lang;
}
const changeLang = (loc) => {
  usei18n.locale.value = loc
  localStorage.lang = loc;
   isOpen.value =false;
};



if(Cookies.get('lightTheme')){
  document.querySelector('html').setAttribute('data-themeLight',Cookies.get('lightTheme')); 
}
/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "160px";
  document.getElementById("main").style.marginLeft = "250px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";

}
const isOpen = ref(false);
const Togglebtn = () =>{
isOpen.value = !isOpen.value;
isOpen2.value = false;

}
const isOpen2 = ref(false);
const Togglebtn2 = () =>{
  isOpen2.value = !isOpen2.value;
  isOpen.value = false;
}
const toggleTheme = (bool) =>{
  document.querySelector('html').setAttribute('data-themeLight',bool);
  Cookies.set('lightTheme',bool);
  isOpen2.value=false;
}



const router = useRouter();
const goToNewPage = () => {
  router.push(`/Search/${searchInput.value}`);
  // const searcText = searchInput.value
  searchInput.value = "";
};
const searchInput = ref("");
// const searchInputChange = (x) =>{
//   searchInput.value = x;
// }

</script>

<template>
  <main>
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="https://fontawesome.com/icons/">
      <title>Nusay Yollary</title>
    </head>
  

    <header class="header all">
          <div class="body">
            <!-- Top Bar -->
         <section>
             <div class="top-bar">
               <div class="lang-selection flex-center" >
                   <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-globe"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg><button class="dropbtn "  @click="Togglebtn()" >
                    {{ $t('dil') }} <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 -960 960 960" width="20"><path d="M480-360 280-560h400L480-360Z"/></svg></button>
                   <div class="lang-content" v-if="isOpen">
                       <a href="#" @click="changeLang('tk')">Türkmence</a>
                       <!-- <a href="#" @click="changeLang('en')">English</a> -->
                       <a href="#" @click="changeLang('ru')">Русский</a>
                   </div>
                 </div>
                 <div class="lang-selection flex-center">
                  <svg width="16px" height="16px"  viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                  <path  d="M12,22 C17.5228475,22 22,17.5228475 22,12 C22,6.4771525 17.5228475,2 12,2 C6.4771525,2 2,6.4771525 2,12 C2,17.5228475 6.4771525,22 12,22 Z M12,20.5 L12,3.5 C16.6944204,3.5 20.5,7.30557963 20.5,12 C20.5,16.6944204 16.6944204,20.5 12,20.5 Z" style="fill: var(--color-text);"></path></svg>
                   <button class="dropbtn" @click="Togglebtn2()">{{ $t('tema') }}
                    <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 -960 960 960" width="20"><path  d="M480-360 280-560h400L480-360Z"/></svg></button>
                   <div class="lang-content" v-if="isOpen2">
                       <a href="#" class="theme"  @click="toggleTheme('true')">{{ $t('ak') }}</a>
                       <a href="#" class="theme"  @click="toggleTheme('false')">{{ $t('gara') }}</a>
                     </div>
                 </div>
             </div>
         </section>
         
          </div>
       
       
       <!-- Navbar -->
       <div class="navbar">
         <nav > 
           <ul>
             <router-link to="/"> <img class="logo" src="./assets/logo-ar.png" width="100px" /> </router-link> 
             <a href="#" class="navlink">{{ $t('Biz_Barada') }}</a>
             <a href="#" class="navlink">{{ $t('Habarlashmak') }}</a>
             <!-- <router-link class="navlink" >{{ $t('Biz_Barada') }}</router-link>
             <router-link class="navlink" >{{ $t('Habarlashmak') }}</router-link> -->
             <li class='search-box'>
               <form class="search-form" @submit="(e)=>{e.preventDefault();goToNewPage();
               }">
                 <input style="width: 100%;" :placeholder= "$t('haryt_gözle')" v-model="searchInput"  />
                 
                 <span @click="goToNewPage"><img src="./assets/search-alt-2-svgrepo-com.svg"  @click="(e)=>goToNewPage(e.currentTarget.value)"  alt=""></span>

                 <!-- <li v-for="item in searchResults" :key="item.id" >{{ item.title }}</li> -->
                </form>
              </li>
              <div class="menu-bar" style="margin-left: auto;">
                <li class='search-box'>
                  <form class="search-formm" @submit="(e)=>{e.preventDefault();goToNewPage();}">
                    <input  type='text' :placeholder="$t('haryt_gözle')" v-model="searchInput"/>
                    <span><img src="./assets/search-alt-2-svgrepo-com.svg"  alt=""  @click="(e)=>goToNewPage(e.currentTarget.value)"></span>
                  </form>
                </li>              
                <div id="mySidenav" class="sidenav">
                  <a href="javascript:void(0)" class="closebtn" @click="closeNav()">&times;</a>
                  <a href="#" class="navlink">{{ $t('Biz_Barada') }}</a>
                  <a href="#" class="navlink">{{ $t('Habarlashmak') }}</a>
                  <div class="dropdown"> 
                    <button class="dropbtnn"  @click="Togglebtn">{{ $t('dil') }}</button>
                    <div class="dropdown-content" v-if="isOpen" id="langbtn">
                      <a href="#"  @click="changeLang('tk')">Turkmence</a>
                      <!-- <a href="#" @click="changeLang('en')">English</a> -->
                      <a href="#"  @click="changeLang('ru')">Русский</a>
                    </div>
                    <div>
                      <button class="dropbtnn" @click="Togglebtn2()">{{ $t('tema') }}</button>
                      <div class="dropdown-content" v-if="isOpen2" id="langbtn">
                        <a href="#" @click="toggleTheme('true')">{{ $t('ak') }}</a>
                        <a href="#" @click="toggleTheme('false')">{{ $t('gara') }}</a>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="burger_span">
                  <router-link to="/"> <img style="width: 100px;" src="./assets/logo-ar.png"  /> </router-link> 
                  <span class="burger" @click="openNav()"> <svg xmlns="http://www.w3.org/2000/svg" height="28" width="28" style="margin-bottom:-20px;" viewBox="0 0 448 512"><path style="fill: var(--color-text);" opacity="1" fill="#1E3050" d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"/> </svg> </span>
                </div>
              </div>
            </ul> 
          </nav>
        </div>
      </header>
      <RouterView></RouterView>

  <!--Footer-->
  <footer style="background-color: #e6e6e6; text-align: center;">
    <div class="footer all">
              <div class="logo" id="footLog">
                  <img src="./assets/logo-ar.png" alt="Logo">
              </div>
              <div class="flex-center footerDetailsCont">
                <div class="address ">
                  <div>
                    <div>
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-map-pin"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    </div>
                    <p style="width: 80%;">G.Kulyyew (Obezdnoý) köçesi Serpaý Binasy Dükan No59, Aşgabat, Türkmenistan </p>
                  </div>
                <!-- <div>
                  <div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-map-pin"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                  </div>
                  <p>Duralga Bus Stop, Daşoguz, Turkmenistan</p>
                </div> -->
                <div>
                  <div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-phone"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  </div>
                  <p>754219</p>
                </div>
                <div class="icons">
                  <a href="https://www.instagram.com/abraylyrysgal/#"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" style="margin-left: 0;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                  <p>abraylyrysgal</p>
                </div>
            </div>
            <div class="link">
              <ul>
                <li ><a href="#">{{ $t('Biz_Barada') }}</a></li>
                <li ><a href="#">{{ $t('Habarlashmak') }}</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div style="background-color: var(--color-footer);"><p style="color: var(--color-text); font-size: x-small;">Made with <s>love</s>  brain by sanly.proMa</p></div>
  </footer>
  </main>

</template>

<script>
   
</script>

<style>
*{
    /* montserrat-regular - cyrillic-ext_latin-ext */
  font-display: swap; /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  src: url('./assets/montserrat-v26-cyrillic-ext_latin-ext-regular.woff2') format('woff2'); /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
  margin: 0;
  padding: 0;
}

  .all{
    width:1000px;
    margin:auto;
  }
  .menu-bar{
    display: none;
  }
  .top-bar{
    background-color: var(--color-navbar) ;
    color: #fff;
    display: flex;
    justify-content: flex-end;
  }
  .logo{
    width: 100px;
  }
  .top-bar img{
    width: 20px;
  height: 20px;
  /* padding-top: 7px; */
  }
  .lang-selection {
    position: relative;
    display: inline-block;
  }
  .lang-selection .lang-content {
    top:2rem;
    position: absolute;
    left: 0;
    background-color: var(--color-footer);
    min-width: 160px;
    z-index: 1;
    /* transform: translateX(40%); */
  }
  .lang-selection .dropbtn {
    background: none;
    padding: 6px;
    font-size: 16px;
    border: none;
    cursor: pointer;
  }
  .lang-selection .lang-content a{
    /* color: black; */
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }

  .lang-selection .lang-content a:hover {
    background-color: #f1f1f1;
  }
  .lang-selection img{
    width: 16px;
    height: 16px;
  }
  .lang-selection button{
    display: flex;
    align-items: center;
    fill: var(--color-text);
  }
/* Navbar*/
.navbar {
      padding: 0 0 20px;
      background-color:var(--color-navbar);
      /* border-bottom: 3px dashed var(--color-border); */
}
  .navbar nav {
      display: flex;
      align-items: center;
  }
  .navbar ul {
    width:100%;
    display: flex;
    align-items: center;
      list-style: none;
      margin: 0;
      padding: 20px;
  }
  
  .navbar li {
      display: inline-block;
      margin-right: 20px;
  }
  
  .navbar a {
      text-decoration: none;
      margin-right: 15px;
      /* color: #333; */
  
  }
    .navbar img {
      vertical-align: middle;
  }
  
  .search-box {
      position: relative;
      margin-left: auto;
      margin-right: 0 !important;
      width: 50%;
  }
  .search-form {
    display: flex;
    background-color: #e6e6e6;
    border-radius: 4px;
    border: 1px solid #ccc;
    justify-content: space-between;
    width: 100%;
  }
  .search-form span {
    width: 25px;
    height: 25px;
    padding-top: 5px;
    
  }
  .search-form img{
    width: 16px;
    height: 16px;
  }
  .search-box input {
    all: none;
    background: none;
    border: none;
    padding: 5px 10px;
    outline: none;
    border-radius: 4px;
    padding: 9px;
  }
  .search-box input:focus {
      outline: none;
      border-color: #888;
  }
  /* Footer Styles */
  .footer {
    /* background-color: #e6e6e6; */
    /* color: #fff; */
    padding: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 3rem;
    width: auto;
    background-color: var(--color-footer) ;
  }
    .footer ul {
        text-align:left;
  }
  .footer .link {
    align-self:flex-start;
  }
  .address svg{
    width: 16px;
    height: 16px;
    margin-right: 5px;
  }
  
  .footer .logo img{
    max-width: 100px;
    justify-content: flex-start;
    padding-bottom: 50px;
  }
  .footer .address {
    display: flex;
    flex-direction: column;
    margin: 0 20px;
  }
  .footer .address div {
    display: flex;
    align-items: baseline;
  }
  .footer .address div div {
    display: flex;
    align-items: center;
  }
  .footer .address div p {
    font-size: 16px;
    margin: 5px 0;
    text-align: left;
  }
  .footer .link {
    display: flex;
    flex-direction: column;
    margin: 0 20px;
    padding-bottom: 63px;
  }
  .footer .link li {
    margin: 5px 0;
    text-decoration: none;
    color: black;
  }
  .link ul li{
    list-style: none;
  }
  .link a{
    text-decoration: none;
  
  }
  .icons{
    display: flex;
    /* justify-content:space-between; */
    margin-top:1rem;
  }
  .icons svg{
      height: 16px;
      width: 16px;
      display: flex;
      text-align: center; 
      margin-left: 20px ;
      stroke: var(--color-text);
      
    }
    
   @media screen and (max-width: 1000px){
    .all{width:auto}
    

   } 
    
    @media screen and (max-width:900px) {
      .all{
       /* width: 150% !important; */
       width: auto;
       text-align: center;
       display: flex;
       justify-content: center;
       flex-direction: column;
      }
      .navbar{
        margin: 0 0.5rem;
      }
      .navbar ul{
        padding: 5px;
      }
      .top-bar{
        /* margin: 0 2rem; */
      }
      .theme{
        text-align: left;
      }
      .lang-selection .lang-content{
        min-width: 0;
      }
    }
 
    @media screen and (max-width:720px) {
      .footer{
        display: flex;
        flex-direction: column;
        column-gap: 2rem;
        padding: 10px;
      }
      .footer ul {
        padding-left:0;

      }
      .lang-selection .lang-content{
        min-width: 0;
      }

    }
    
   @media screen and (max-width: 600px){ 
     .all{
       width: auto;
      }
      .search-form{
        display: none;
      }
    .logo{
      display: none;
    }
    #footLog{
      display: flex;
    }
    .bar_logo{
      width: 100px;
    }
      .search-formm{
    display: flex;
    background-color: #e6e6e6;
    border-radius: 4px;
    border: 1px solid #ccc;
    justify-content: space-between;
}
.navbar{
  margin: 0;
  padding: 0;
}
.burger_span{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 5px;
}
  .navbar ul{
    display: block;
    margin: 0 10px 0 10px;
    padding: 0;
  }
  .navlink{
    display: none;
  }
    .menu-bar{
      display: flex;
    flex-direction: column-reverse;
    padding-bottom: 5px;
    }
    .menu-bar span{
      margin-right: 5px;
      margin-left: 10px;
      height: 28px;
      width: 22px;
    }
    .menu-bar span img{
      width: 20px;
      height: 20px;
    }
      .top-bar{
        display: none;
      }
      .headerLi{
        display: none!important;
      }
      .search-box{
        margin-left: 0 !important;
        width: auto;
      }
  .search-box input {
    width: 100%;
    all: none;
    background: none;
    border: none;
    padding: 8px 8px;
    outline: none;
    border-radius: 4px;
    
  }
  .search-box span {
    padding-top: 5px;
    margin-right: 5px;
  }
      /* .footer .flex-center{
        flex-direction: column;
      } */
      .footer{
        display: flex;
        flex-direction: column;
        column-gap: 2rem;
        padding: 10px;
      }
      .footer .logo img{
        padding: 0;
      }
        /* The side navigation menu */
.sidenav {
  height: 100%; /* 100% Full-height */
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed; /* Stay in place */
  z-index: 3; /* Stay on top */
  top: 0; /* Stay at the top */
  right: 0;
  background-color:  #e6e6e6; /* Black*/
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 60px; /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
  /* padding-left: 1rem; */
  text-align: left;
  background-color: var(--color-navbar);
}

/* The navigation menu links */
.sidenav a {
  padding-top: 8px;
  text-decoration: none;
  font-size: 25px;
  /* color: #818181; */
  display: block;
  transition: 0.3s;
  padding-left: 1rem;
  
}
.sidenav button{
  padding-left: 1rem ;
}
/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  color: #f1f1f1;
}
.sidenav a{
  font-size: 18px;
}
/* Position and style the close button (top right corner) */
.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  text-align: left;
  margin-right: 65%;
}
/* Style page content - use this if you want to push the page content to the right when you open the side navigation */
#main {
  transition: margin-left .5s;
  padding: 20px;
}
.dropbtnn {
  background-color:var(--color-navbar);
  /* color: #818181; */
  padding: 5px 0;
  font-size: 18px;
  border: none;
}
.dropdown {
  position: relative;
  display: inline-block;
}
/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #e6e6e6;
  min-width: 160px;
  /* box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); */
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: #818181;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  margin-right: 45px;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: block;}
} 

@media screen and (max-width:500px) {
    .footerDetailsCont{
      flex-direction:column;  
    
    }
  }

@media screen and (max-width: 450px){
  .bar_logo{
    width: 100px;
  }
  .logo{
    display: none
  }
  .navbar img{
    padding-bottom: 10px;
  }
  .search-form{
    display: none;
}
.navbar{
  padding: 0;
  margin: 5px;
}
.navbar ul{
  padding: 0;
}
  .search-formm{
    display: flex;
    background-color: #e6e6e6;
    border-radius: 4px;
    border: 1px solid #ccc;
    justify-content: space-between;
}
.search-formm span{
  width: 25px;
  height: 25px;
}
.search-formm img{
    width: 16px;
    height: 16px;
  }
  .navbar ul{
    display: block
  }
  .menu-bar{
    display: flex;
    flex-direction: column-reverse;
    padding-bottom: 5px;
  }
  .burger_span{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
  .burger{
    margin-right: 10px;
  }
    }


</style>