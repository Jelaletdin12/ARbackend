<template>
    <main>
<div class="news CONT" v-if="tazelikler">
<h1>{{ tazelikler.Tazeligiň_ady}}</h1>

      <div class='flex'>
        <p style='width:auto;line-height:1.5; margin: 10px;' >
       {{ tazelikler.Tazeligiň_maglumaty }}
        </p>
        <img :src='tazelikler.Tazeligiň_suraty' class='mainSideImg'>
      </div>
 </div>
    </main>
</template>


<script>
 import { useI18n } from 'vue-i18n';
import axios from 'axios';
export default {
  props:['id'],
  data() {
      return {
        tazelikler: null,
  }
  },
  mounted() {
    this.fetchtazelikler();
    const locale = useI18n()
    this.$watch(()=>locale.locale.value,(loc)=>{
      window.location.reload();  
    })
    window.scrollTo(0, 0);
  },
  methods: {
    async fetchtazelikler() {
      try {
        
        const locale = useI18n()
        const headers = {}
        headers["Accept-Language"] = locale.locale.value;

        const response = await axios.get(`http://127.0.0.1:8000/tazelikler/api/tazelikler/${this.$route.params.id}`, {headers});
        this.tazelikler = response.data;
        console.log(response, this.tazelikler.id);
      } catch (error) {
        console.error('Error fetching tazelikler:', error);
      }
    },
}}

</script>

<style scoped>

* {
  font-display: swap; /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  src: url('./assets/montserrat-v26-cyrillic-ext_latin-ext-regular.woff2') format('woff2'); /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
  
}

.CONT{
  width:1000px;
  margin:auto;
}
/* nav ul{
    display: flex;
    align-items: center;
    list-style:none;
    padding:0;
} */
h1{
  line-height: 1.2;
  position: relative;
  margin:4rem;
  margin-left:2rem;
  margin-right:0;
}
h1::before{
  content:'';
  position: absolute;
  top:0;
  left:-2rem;
  background-color: red;
  width:1rem;
  height: 100%;
}

.mainSideImg{
  width: 50%;
  padding: 20px;
}
@media screen and (max-width:1000px) {
  .CONT{
    width: auto;
  }
}
@media screen and (max-width:900px) {
      .CONT{
        width: auto;
      }
      .flex{
        display: flex;
        flex-direction: column; 
      }
    .flex p{
      margin-left: 15px;
    }
    .CONT h1{
      font-size: x-large;
    }
    .mainSideImg{
  width: auto;
}

    }
@media screen and (max-width: 600px){ 
  .CONT{
  width:auto;
  }
  h1{
  font-size:1.5rem;
}
h1::before{
  margin: 5px;
}
.mainSideImg{
  width: 85%;
  padding: 20px;
  margin-left: 23px;
}
.flex p{
  margin: 24px;
  font-size: medium;
}
.flex{
  flex-direction: column;
}
}
@media screen and (max-width: 450px) { 
  .mainSideImg{
    margin-left: 6px;
  }
}
</style>