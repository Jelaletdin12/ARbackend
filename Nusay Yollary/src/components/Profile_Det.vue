<template>
    <main>

    <div class="content g-margin" >
        <div v-if="profiller">
          <h1 class="h1"> {{ profiller.Profiliň_ady }}</h1> <br>
          <div class="details">
            <div style="width: 50%;" id="det">
              <p class="text"> {{  profiller.Maglumat }}</p>
              <p>{{ $t('salgy') }}: {{ profiller.Salgy }}</p>
              <p>{{ $t('tel_belgi') }}: {{ profiller.Tel_belgiler }}</p>
              <p>{{ $t('mail') }}: {{ profiller.Mail }}</p>
            </div>
              <div class="dtl-img">
                <img :src='profiller.Surat' alt="">
              </div>
          </div>
        </div>

    <div class="news">
        <h1 style="padding-bottom: 25px; padding-top: 100px;">{{ $t('tazelikler') }}</h1>
        <div class="news-img-cont">
            <div class="news-img" v-for="tazelikler in tazelikler" :key="tazelikler.id">
              <img :src="tazelikler.Tazeligiň_suraty"  @click="goToNewPage(tazelikler.id)">
              <p >{{ tazelikler.Tazeligiň_ady }}</p>
            </div>
        </div>
    </div>

 
        
        <h1 style="color: var(--color-habarp); padding-bottom: 25px;">{{ $t('suratlar') }}</h1>

        <div class="photos" v-if="profiller">
        <img v-for="img in profiller.images" :key="img.id" :src="img.image" alt="" @click="openImageModal(img.image)">
        </div>

        <!-- The Modal -->
<div id="myModal" class="modal">
  <span class="close" @click="closeModal">&times;</span>
  <span class="arrow left-arrow" @click="prevImage">&#10094;</span>
  <img class="modal-content" :src="selectedImage" id="img01">
  <span class="arrow right-arrow" @click="nextImage">&#10095;</span>
  <div id="caption"></div>
</div>

    </div>

</main>
</template>


<script>
import { onMounted, ref, watch } from 'vue';
import axios from 'axios';
import { useI18n } from 'vue-i18n';
export default {

  
  props: ['id'],
  data() {
      return {
        tazelikler: [],
        profiller:null,
        selectedImage: null,
  }
  },
  mounted() {
    const locale = useI18n()

    this.fetchtazelikler();
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
        
        const response = await axios.get('http://127.0.0.1:8000/tazelikler/api/tazelikler/');
        const resProfil = await axios.get(`http://127.0.0.1:8000/api/profiller/profile/${this.$route.params.id}`,
        {headers:headers}
        );



        this.tazelikler = response.data;
        this.profiller = resProfil.data;
        console.log(resProfil.data, 'dataa')
        // this.translatedMaglumat =  t('Maglumat', this.profiller.Maglumat);
      } catch (error) {
        console.error('Error fetching:', error);
      }
  },
  goToNewPage(id){
    this.$router.push(`/News/${id}`)
  },

  openImageModal(image) {
      this.selectedImage = image;
      const modal = document.getElementById('myModal');
      modal.style.display = 'block';
    },
    closeModal() {
      this.selectedImage = null;
      const modal = document.getElementById('myModal');
      modal.style.display = 'none';
    },
    prevImage() {
      // Önceki resmi gösteren fonksiyon
      const currentIndex = this.profiller.images.findIndex(img => img.image === this.selectedImage);
      if (currentIndex > 0) {
        this.selectedImage = this.profiller.images[currentIndex - 1].image;
      }
    },

    nextImage() {
      // Sonraki resmi gösteren fonksiyon
      const currentIndex = this.profiller.images.findIndex(img => img.image === this.selectedImage);
      if (currentIndex < this.profiller.images.length - 1) {
        this.selectedImage = this.profiller.images[currentIndex + 1].image;
      }
    },
  }
}
</script>

<style scoped>
    /* Style the contenet div */
    *{
      font-display: swap; /* Check https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display for other options. */
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 400;
  src: url('./assets/montserrat-v26-cyrillic-ext_latin-ext-regular.woff2') format('woff2'); /* Chrome 36+, Opera 23+, Firefox 39+, Safari 12+, iOS 10+ */
  
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
}

/* Modal Content (image) */
.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

/* Caption of Modal Image */
#caption {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  text-align: center;
  color: #ccc;
  padding: 10px 0;
  height: 150px;
}

/* Add Animation */
.modal-content, #caption {  
  -webkit-animation-name: zoom;
  -webkit-animation-duration: 0.6s;
  animation-name: zoom;
  animation-duration: 0.6s;
}

@-webkit-keyframes zoom {
  from {-webkit-transform:scale(0)} 
  to {-webkit-transform:scale(1)}
}

@keyframes zoom {
  from {transform:scale(0)} 
  to {transform:scale(1)}
}

/* The Close Button */
.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}

/* 100% Image Width on Smaller Screens */
/* @media only screen and (max-width: 700px){
  .modal-content {
    width: 100%;
  }
} */
.arrow {
  position: absolute;
    top: 50%;
    width: 40px;
    height: 40px;
    margin-top: -20px;
    font-size: 30px;
    cursor: pointer;
    color: #fff;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
}
.left-arrow {
    left: 10px;
    padding-bottom: 4px;
  }

  .right-arrow {
    right: 10px;
    padding-bottom: 4px;
  }

.content {
    display: flex;
    flex-direction: column;
    width: 80%;
    margin: 0 auto;
    padding: 20px;
    justify-content: space-around;
  }
  /* Style the details div */
  .details {
    display: flex;
    flex-direction: row;
    margin-bottom: 20px;
    justify-content: space-between;
  }
  /* Style the h1 tag inside the details div */
  .h1 {
    border-left: 10px solid red;
    padding-left: 10px;
    text-align: left;
    margin-bottom: 10px;
  }
  /* Style the p tag inside the details div */
  .details p {
    font-size: 16px;
    line-height: 1.5;
    margin-top: 10px;
    width: 100%;
  }
  /* Style the img tag inside the details div */
  .dtl-img{
    height: 400px;
    object-fit: cover;
    margin-left: 3rem;
  }  
  .dtl-img img{
    width: 100%;
    height: 100%;
  }
  /* Style the news div */
  .news {
    justify-content: space-between;
    padding-bottom: 100px;
  }
  .news h1{
    color: var(--color-habarp);
  }

  .news-img-cont{
    display: flex;
    flex-wrap: wrap;
    column-gap: 1rem;
  }
  
  /* Style the news-img div */
  .news-img {
    flex: 1;
    margin-bottom: 20px;
  }
  .news-img p{
    display: flex;
    padding: none;
    color: var(--color-habarp);
  }
  /* Style the img tag inside the news-img div */
  .news-img img {
    width: 100%;
    height: 300px;
    object-fit: cover;
  }
  /* Style the h2 tag inside the news-img div */
  .news-img h2 {
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
  }
  /* Style the photos div */
  .photos {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
    justify-content: space-between;
    row-gap: 2rem;
    column-gap: 1.5rem;
  }
  /* Style the img tag inside the photos div */
  .photos img {
    width: 100%;
    height: 225px;
    object-fit: cover;
    /* margin-bottom: 10px; */
  }
.g-margin{
  display: block;
  width: 980px;
  margin: auto;
}
@media screen and (max-width: 1000px){

  .g-margin{
    width: auto;
  }
}
@media screen and (max-width: 900px){
  .content{
    width: auto;
  }
  .dtl-img{
    margin-left: 5px;
    padding-right: 5px;
  }
  .news-img img{
    height: 250px;
  }
  .photos img{
    /* height: 300px;
    width: auto; */
    justify-content: space-evenly;
  }
  
    
}
@media screen and (max-width: 800px) {
      .details{
        display: flex;
        flex-direction: column-reverse;
      }
      #det{
        width: auto !important;
      }
    }
@media screen and (max-width: 600px){ 
  /* General styling */
  .content, .news, .photos {
    width: auto;
    margin: 0 auto;
  }
  /* Heading styling */
  .h1 {
    font-size: 30px;
    margin-bottom: 20px;
  }
  /* Details section styling */
  .details {
    display: flex;
    flex-direction: column-reverse;
    align-items: auto;
  }
  .details img{
    width: 100%;
    height: 100%;
  }
  .dtl-img{
  margin-left: 0;
  }
  .details p{
    width: auto;
      }
  .news-img-cont {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .news-img {
    margin: none;
  }
  .news-img img {
    width: 100%;
    height: 150px;
  }
  .photos img {
    width: 100%;
    height: 145px;
  }
  #det{
    width: auto !important;
  }
}
</style>