<template>
  
  <div style="margin-left: 10px;">
    <h2 class="sowda">Gözlenen</h2>
  </div>
  <div class="cards">
    <div class="card-img" v-for="profil in profiller" :key="profil.id">
      <img :src="profil.Surat" alt="" @click="goToNewPage(profil.id)">
      <p>{{ profil.Profiliň_ady }}</p>
    </div  >
    <div v-if="profiller && profiller.length === 0" class="no-results-message">
      Netije tapylmady.
    </div>

    

  </div>
</template>


<script>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
import axios from 'axios';
import { useI18n } from 'vue-i18n';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const x = route.params.txt;
    const profiller = ref([]);
    const i18n = useI18n();
    
    const fetchprofiller = async (searchText) => {
      try {
        console.log(x);
        const headers = {
          'Accept-Language': i18n.locale.value,
        };
        const response = await axios.get(`http://127.0.0.1:8000/api/profiller/profile?search=${searchText}`, { headers });
        profiller.value = response.data;
        console.log(response.data);
        
      } catch (error) {
        console.error('Error fetching:', error);
      }
    };
    const goToNewPage = (id) =>{
    router.push(`/Profile_Det/${id}`)}
    // Watch kullanarak searchText değiştiğinde fetchData fonksiyonunu çağırma
    watch(() => route.params.txt,() => {
      fetchprofiller(route.params.txt);
      console.log("123");
      // window.location.reload();
    });

    onMounted(() => {
      // İlk yükleme için fetchData fonksiyonunu çağır
      fetchprofiller(x);
      
    });

    return { x, profiller, goToNewPage };
    
  },
  
};

</script>


<style>
/* Add this to your existing styles */

.sowda{
    border-left: 10px solid red;
    padding-left: 10px;
    text-align: left;
    margin-bottom: 25px;
    margin-top: 50px;
    font-weight: 700;
}
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
    justify-content: space-between;
    row-gap: 2rem 
}
  .card-img {
    padding: 10px;
    margin-bottom: 20px;
}
  /* Style the .card-img img element */
.card-img img {
    width: 225px;
    height:225px;
    object-fit: cover;
}
.card-img h2 {
    text-align: center;
    margin-top: 10px;
}
.card-img p{
  font-display: swap; 
  font-weight: 300;
  margin: 0;
}
.no-results-message {
  text-align: center;
  margin: 20px;
  font-weight: bold;
  color: red;
}

@media screen and (min-width:1000px) {
  .cards {
    grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
   }
}
@media screen and (max-width: 600px){ 
  .cards{
    justify-content: center;
  }
  .card-img{
    width: auto;
  }
}

</style>