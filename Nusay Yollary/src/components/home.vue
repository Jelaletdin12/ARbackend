<template>
  <main>
    
  <div class="all" >
      <Splide :options="{autoplay:true, rewind: true, interval: 4000, gap:'1rem', arrows: hide,  mediaQuery:'min',breakpoints:{360:{height:'100%'}}}" aria-label="My Favorite Images" class="splide" >
      <SplideSlide  v-for="banner in banners" :key="banner.id">
       <a :href='banner.Link'><img  class="slide-img" :src="banner.Surat" alt="Sample 1"></a>
      </SplideSlide>
    </Splide>
    

        <div style="margin-left: 10px;">
          <h2 class="sowda">{{ $t('sowda_nokat') }}</h2>
        </div>
        <div class="cards">
          <div class="card-img" v-for="profiller in profiller" :key="profiller.id">
            <img :src="profiller.Surat" alt="" @click="goToNewPage(profiller.id)">
            <p>{{ profiller.Profiliň_ady }}</p>
          </div  >
        </div>
        <div class="dovamy"> 
          <button >{{ $t('dowamy') }}
            <svg xmlns="http://www.w3.org/2000/svg" style="fill: white;" height="20" viewBox="0 -960 960 960" width="20"><path d="M480-345 240-585l56-56 184 184 184-184 56 56-240 240Z"/></svg>
          </button>
        </div>
          
        <div class="about" >
          <div class="logo">
                <img src="../assets/logo-ar.png" alt="Logo">
            </div>
          <div style="display: flex;">
            <h1 style="font-weight: 600;">Abrayly Rysgal</h1> 
            <!-- <h1 style="margin-left: 6px;"> {{ $t('topar') }}</h1> -->
          </div>
          <div>
            <!-- <p> Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p> -->
            <div class="red-line">
              <span></span>
            </div>
          </div>
        </div>
    
        <div class="contact">
          <div class="for-contact" style="flex:1">
          <h2 style="border-left: 10px solid red; padding:0 0 0 10px;"> {{ $t('habarlashmak_un') }}</h2>
          <div class="flex-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-map-pin"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
           <p>G.Kulyyew (Obezdnoý) köçesi Serpaý Binasy Dükan No59, Aşgabat,  Türkmenistan</p>
          </div>
          
          <div class="flex-center"  >
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-phone"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <p>754219</p>
          </div>
          <div class="icons">
                <a href="https://www.instagram.com/abraylyrysgal/#"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                <p>abraylyrysgal</p>
             </div>
        </div>
    
        <div class="feedback-form">
        <form action="#">
          <div class="form-group">
            <label for="name">{{ $t('at') }}</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-group">
            <label for="email">{{ $t('mail') }}</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-group">
            <label for="message">{{ $t('hat') }}</label>
            <textarea id="message" name="message" rows="15" required></textarea>
          </div>
          <button type="submit">{{ $t('ugrat') }}</button>
          </form>
        </div>
        </div>
      </div>
  </main>
    </template>
  
  
  <script>
    import { useI18n } from 'vue-i18n';
    import axios from 'axios';
    import { onMounted, ref } from 'vue';
    import { Splide, SplideSlide} from '@splidejs/vue-splide';
    import '@splidejs/vue-splide/css/skyblue';
    import "@splidejs/splide/dist/css/themes/splide-default.min.css";
    import '@splidejs/splide/dist/js/splide'
    import { AutoScroll } from '@splidejs/splide-extension-auto-scroll';
    import { defineComponent } from 'vue';
     export default defineComponent({
      name: 'Nusay Yollary',
      components:{AutoScroll, Splide, SplideSlide },
      data() {
      return {
        profiller: [],
        banners: [],
  }
  },
  mounted() {
    const locale = useI18n()
    this.fetchProfiller();
    this.$watch(()=>locale.locale.value,(loc)=>{
      window.location.reload();  
    });
    window.scrollTo(0, 0);
  },
  methods: {
    async fetchProfiller() {
      try {

        const locale = useI18n()
        const headers = {}
        headers["Accept-Language"] = locale.locale.value;

        const response = await axios.get('http://127.0.0.1:8000/api/profiller/profile/', {headers:headers});
        const bannerRes = await axios.get('http://127.0.0.1:8000/banners/api/bannerler/');
        this.profiller = response.data.reverse();
        this.banners =  bannerRes.data;
      } catch (error) {
        console.error('Error fetching banners:', error);
      }

    },
  goToNewPage(id){
    this.$router.push(`/Profile_Det/${id}`)
  },
  
  }
  
  })

  

</script>
  
  
  <style scoped>

  *{
    font-display: swap; /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  src: url('./assets/montserrat-v26-cyrillic-ext_latin-ext-regular.woff2') format('woff2'); /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
  
}


  .all{
    width:1000px;
    margin:auto;
    padding-bottom: 50px;
    
  }
  .splide{
    padding: 10px;
  }
  /* slider */
  .slider-h2 {
    position: absolute;
    top: 0;
    left: 10px;
    color: wheat;
  }
  /* Style the .cards container */
  .cards {
    display: grid;
    grid-auto-rows: 250px;
    grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
    justify-content: space-between;
    row-gap: 1rem 
  }
  /* Style the .card-img element */
  .card-img {
    padding: 10px;
    margin-bottom: 20px;
  }
  /* Style the .card-img img element */
  .card-img img {
    width: 100%;
    /* height: 100%; */
    object-fit: cover;
  }
  /* Style the .card-img h2 element */
  .card-img h2 {
    text-align: center;
    margin-top: 10px;
  }
  .card-img p{
  font-display: swap; 
  font-weight: 300;
  margin: 0;
  }

  .dovamy{
  display: flex; 
  justify-content: center; 
  margin-top: 10px;
  }
  .dovamy button{
  width: 160px; 
  justify-content: center;
  display: flex; 
  align-items: center;
  }
.sowda{
    border-left: 10px solid red;
    padding-left: 10px;
    text-align: left;
    margin-bottom: 25px;
    margin-top: 50px;
    font-weight: 700;
}
  .red-line {
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 10px 0;
  }
  .red-line span {
    display: block;
    width: 20%;
    background-color: red;
    height: 10px;
  }
  /* Style the about section */
  .about {
    /* background-color: #fff; */
    padding: 10px;
    margin: 20px 0;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  /* Style the logo */
  .about .logo {
    margin-bottom: 20px;
  }
  .about .logo img {
    width: 100px;
    max-width: 150px;
  }
  /* Style the heading */
  .about h1 { 
    text-align: left;
    margin-bottom: 10px;
    font-size: 24px;
  }
  /* Style the paragraph */
  .about p {
    text-align: justify;
    font-size: 16px;
    line-height: 1.5;
    margin-bottom: 0;
    font-display: swap; 
    font-family: 'Poppins';
    /* font-style: italic; */
  }
  .contact{
    display: flex;
    justify-content: space-around;
  }
  .contact p{
    text-align: left;
  }
  .contact svg{
    min-width: 16px !important;
    height: 16px;
    margin-right: 5px;
  }
  .icons{
    display: flex;
  }
  .icons svg{
      height: 16px;
      width: 16px;
      display: flex;
      text-align: center;
      margin-left: 0;
      stroke: var(--color-text);
    }
    .icons svg:not(:first-child){
      margin-left:1rem;
    }
    .for-contact{
      margin-left: 10px;
    }
  /* Style the feedback form */
  .feedback-form {
    width: 400px;
    margin: 0 auto;
    padding: 20px;
    justify-content: end;
  }
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  /* Style the form group */
  .form-group {
    margin-bottom: 10px;
  }
  .form-group label{
    display: inline-block;
    margin-bottom: 5px;
  }
  input, textarea {
    box-sizing: border-box;
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
    background-color: #e6e6e6
  }
  select {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
  }
  button {
    width: 100%;
    background-color: red;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin: 0 !important;
  }
  .slide-img{
  width: 100%;
  /* height: 100%; */
}

@media screen and (min-width:1000px) {
  .cards {
    grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
   }
}
@media screen and (max-width:1000px) {
  .all{
    width:auto;
  }
  
}
@media screen and (max-width:900px) {
  .all{
   width: auto;
  }
  .for-contact{
  margin-left: 10px;
  }
  .contact svg{
    width: 16px;
    height: 16px;
}
}
@media screen and (max-width:800px) {
  .contact{
    display: flex;
    flex-direction: column;
  }
  
}

@media screen and (max-width: 620px){
  /* .cards {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    justify-content: space-between;
    row-gap: 2rem 
  } */
}
  

 @media screen and (max-width: 600px){ 
  .cards{
    justify-content: center;
  }
  .all{
    width:auto;
  
  }
  .card-img{
    width: auto;
  }
  .contact{
    display: flex;
    flex-direction: column;
  }
  .for-contact{
    margin-left: 25px;
  }
  .about .logo {
    /* display: flex;
    justify-content: center; */
    text-align: center;
  }
  .feedback-form{
    width: auto;
  }
}
  </style>