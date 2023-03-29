<template>
  <v-row style="height: 100%" no-gutters>

    <v-col cols="12" md="9"
      class="pa-1"
      style="height: 100%" 
      no-gutters  >

      <div
        class="video-canvas-container"
      >
      <!--
        style="width:100%;
        height: 80%;
        position:relative;"
      -->

      <!-- vjs-static-controls - чтобы вынести элементы управления за видеоповерхность -->
        <video
          preload="auto"
          controls
          id="video-id"
          
          class="video video-js
            vjs-static-controls
            vjs-nofull"
        >

        <!-- 
          onplay="resize_canvas(this)"
          data-setup='{"customControlsOnMobile": true}'

          style="
          position:relative;
          top:0;left:0;
          width:100%;
          height: 100%;
          hidden;"
          -->
          
          <source src="video_example.mp4" type="video/mp4">
        </video>

        <canvas id="video-canvas-id"
          class="canvas"
        >
        <!-- 
          style="position:absolute;
          top: 0;
          left: 0;
          z-index: 100;"
          -->
        </canvas> 

      </div>

      <v-card 
        class="pa-1 mt-1"
        no-gutters
        style="height: 30%"
        >

        <v-card-title class="ma-0 pa-0">
          Фильтры
          <v-spacer/>
          <v-switch
            v-model="filtersOn"
          ></v-switch>

          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <v-chip
                v-bind="attrs"
                v-on="on"
              ><v-icon>mdi-help</v-icon></v-chip>
            </template>
            <span>
              Фильтры цвета (слайдеры) работают на<br/>
              фронтенде и применяются мгновенно,<br/>
              чтобы применить фильтры мерцания<br/>
              и контента, необходимо выбрать один<br/>
              и нажать кнопку "Применить"<br/>
            </span>
          </v-tooltip>
        </v-card-title>

        <v-row class="pa-1">
          <!-- фильтры на фронте - цвета -->
          <v-col>
            <!-- <div style="display: flex;"> -->
              <v-slider dense thumb-label
                label="Насыщен."
                v-model="saturate"
                min="0.0" max="5.0" step="0.1"
              />
              <v-slider dense thumb-label
                label="Яркость"
                v-model="brightness"
                min="0" max="3" step="0.1"
              />
              <v-slider dense thumb-label
                label="Оттенок"
                v-model="hue"
                min="0" max="360" step="1"
              />
            <!-- </div> -->
          </v-col>

          <v-col>
            <!-- <div style="display: flex;"> -->
              <v-slider dense thumb-label
                label="Сепия"
                v-model="sepia"
                min="0" max="1" step="0.05"
              />
              <v-slider dense thumb-label
                label="Контр."
                v-model="contrast"
                min="0" max="5" step="0.05"
              />
            <!-- </div> -->
          </v-col>
          
          <!-- фильтры на беке -->
          <v-col class="pa-1">
            <v-radio-group v-model="backendFilters" dense>
              <v-radio dense
                label="Фильтр мерцания 1"
                value="flickering1"
              ></v-radio>
              <v-radio dense
                label="Фильтр мерцания 2"
                value="flickering2"
              ></v-radio>
              <v-radio dense
                label="Фильтр: курение и сигареты"
                value="smoking"
              ></v-radio>
              <v-radio dense
                label="Фильтр: интимные сцены"
                value="censored"
              ></v-radio>
            </v-radio-group>
            <v-btn disabled>Применить</v-btn>
          </v-col>

          <!-- фильтр на фронте - тип цензуры -->
          <v-col class="pa-1">
            <v-radio-group v-model="censureFilters" dense>
              <v-radio dense
                label="Закрашивние"
                value="fill"
              ></v-radio>
              <v-radio dense
                label="Размытие"
                value="blur"
              ></v-radio>
              <v-radio dense
                label="Пикселизация"
                value="pixelate"
              ></v-radio>
            </v-radio-group>
          </v-col>
          
        </v-row>
      </v-card>
    </v-col>

    <v-col cols="12" md="3"
      class="pa-1"
      style="height: 100%" 
      no-gutters
    >
      <!-- <v-card class="pa-1 my-1">
        <v-card-title>Простейший</v-card-title>

        <v-file-input
          v-model="files"
          counter
          label="File input"
          multiple
          placeholder="Select your files"
          prepend-icon="mdi-paperclip"
          outlined
          :show-size="1000"
        >
          <template v-slot:selection="{ index, text }">
            <v-chip
              v-if="index < 2"
              dark
              label
              small
            >
              {{ text }}
            </v-chip>
      
            <span
              v-else-if="index === 2"
              class="text-overline grey--text text--darken-3 mx-2"
            >
              +{{ files.length - 2 }} File(s)
            </span>
          </template>
        </v-file-input>

      </v-card> -->

      <!-- <v-card
        class="pa-1 my-1"
        style="height: 49%">

        <v-card-title>Filepond</v-card-title>

        <file-pond
          name="filepond"
          ref="pond"
          credits=""
          label-idle="Drop files here..."
          :allow-multiple="true"
          accepted-file-types="image/jpeg, image/png"
          server="/api/filepond"
          :files="filepond_files"
          @init="filepond_init_handler"
        />
      </v-card> -->

      <v-card 
        class="pa-1 my-1"
        style="height: 49%">

        <v-card-title>
          Демо-видео
          <v-spacer/>

          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <v-chip
                v-bind="attrs"
                v-on="on"
              ><v-icon>mdi-help</v-icon></v-chip>
            </template>
            <span>
              Список коротких исходных видео,<br/>
              наиболее наглядно демонстрирующих<br/>
              работу фильтров
            </span>
          </v-tooltip>

        </v-card-title>

        <!-- список видео -->
        <v-list>
          <v-list-item-group
            v-model="selectedVideo"
            color="primary"
            
          >
            <v-list-item
              v-for="(item, i) in videos"
              :key="i"
            >
              <v-list-item-icon>
                <v-icon>mdi-multimedia</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
              {{ Math.floor(item.duration / 60) + ":" + item.duration%60 }}
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>

      <v-card 
        class="pa-1 my-1"
        style="height: 49%">

        <v-card-title>
          Загрузить своё
          <v-spacer/>

          <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
              <v-chip
                v-bind="attrs"
                v-on="on"
              ><v-icon>mdi-help</v-icon></v-chip>
            </template>
            <span>
              Загрузка своего исходного видео<br/>
              чтобы применить к нему фильтры<br/>
              (не более 50 Мб из-за<br/>
              ограничений мощности сервера)
            </span>
          </v-tooltip>

        </v-card-title>

        <dashboard
          :uppy="uppy"
          :plugins="[]"
          :props="{
            theme: 'dark',
            inline: true,
            width:'100%'}"
          ></dashboard>
          <!-- @load="this.parentElement.style.height='70px'" -->
      </v-card>     
    </v-col>
  </v-row>
</template>

<script>


/* подключение для FilePond/vue-file-pond */

// import vueFilePond from "vue-filepond";
// import "filepond/dist/filepond.min.css";
// ниже-плагины, ставить отдельно
// import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css";
// import FilePondPluginFileValidateType from "filepond-plugin-file-validate-type";
// import FilePondPluginImagePreview from "filepond-plugin-image-preview";
// const FilePond = vueFilePond(
//   // плагины, ставить отельно
//   // FilePondPluginFileValidateType,
//   // FilePondPluginImagePreview
// );

/* подключение для Uppy, npm install @uppy/vue @uppy/dashboard @uppy/core @uppy/drag-drop @uppy/progress-bar*/

import { Dashboard } from '@uppy/vue'
// import XHR from '@uppy/xhr-upload' // TODO
// нужно подключить все css для установленных плагинов
import '@uppy/core/dist/style.css'
import '@uppy/dashboard/dist/style.css'
import '@uppy/status-bar/dist/style.css'
import Uppy from '@uppy/core'
// import Webcam from '@uppy/webcam'
// const uppy = new Uppy()//.use(Webcam)

import 'video.js/dist/video-js.css'
import videojs from 'video.js';
import axios from 'axios'


// import { fabric } from 'fabric';

export default {
  name: 'MainView',
  components:{

    /* для filepond */
    // FilePond,

    /* для uppy */
    Dashboard,
  },
  data(){
    return {
      player: null,
      video: null,
      video_canvas : null,
      fabric_canvas: null,
      test_circle: null,
      files : [],
      /* свойства для filepond */
      filepond_files : [], // модель
      canvasInterval : null, // таймер обновления канваса

      filtersOn : true, // отображать фильтрованное или исходное видео
      backendFilters : "",
      censureFilters : "",

      /* https://codepen.io/ygjack/pen/xrqQjR */
      saturate : 1.0, // min="0" max="5" step="0.1" value="1"
      brightness : 1.0, // min="0" max="3" step="0.05" value="0"
      hue : 0.0, // min="0" max="360" step="1" value="0"
      sepia : 0.0, //min="0" max="1" step="0.05" value="0"
      contrast : 1.0, // min="0" max="5" step="0.05" value="1"

      colorfilters : "",

      videos : [
        {
          url:"video_example.mp4", text:"С мерцанием 1",
          duration : "60",
        },
        {
          url:"video_example2.mp4", text:"С мерцанием 2",
          duration:"90",
        },
      ], // список видео для просмотра/обработки
      selectedVideo : null,
      pending_request_id : null,
      percent_ready : 100,
    }
  },
  computed: {
    uppy(){
      
      return new Uppy()//.use(Uppy.Dashboard, {
                // hideUploadButton: true,
                // height: '100%',
                // width: '100%',
                // inline: true})//.use(Webcam)
      }
  },

  methods:{

    /* методы для filepond */
    filepond_init_handler() {
      console.log("FilePond has initialized");
      // FilePond instance methods are available on `this.$refs.pond`
    },

    drawImage() { // обновление кадра
      //var video_ratio = this.video.videoWidth / this.video.videoHeight;
      this.resize_canvas();

      var ctx = this.video_canvas.getContext('2d', { alpha: false });
      // ctx.imageSmoothingEnabled = true;
      ctx.filter = "none";

      // записывать эффекты в промежуточный канвас
      var tmpCanvas = document.createElement("canvas");
      tmpCanvas.width = this.video.videoWidth;
      tmpCanvas.height = this.video.videoHeight;
      var tmpContext = tmpCanvas.getContext('2d');
      tmpContext.drawImage(this.video, 0, 0);
        console.log("*** tmp w h after copy", tmpCanvas.width, tmpCanvas.height);

      // console.log("video.clientWidth = ", this.video.clientWidth);
      // console.log("video.context = ", this.video.getContext('2d'));

      // отобразить всё изображение
      // ctx.drawImage(this.video, 0, 0,
      //   this.video.videoWidth, this.video.videoHeight,
      //   fit_x, fit_y, fit_width, fit_height);
      // ctx.drawImage(this.video, 0, 0,
      //   this.video.offsetWidth, this.video.offsetHeight);
      

      // var blurred_x_src = 200;
      // var blurred_y_src = 200;
      // var blurred_w_src = 200;
      // var blurred_h_src = 200;

      // var blurred_x_trg = blurred_x_src * fit_ratio;
      // var blurred_y_trg = blurred_y_src * fit_ratio;
      // var blurred_w_trg = blurred_w_src * fit_ratio;
      // var blurred_h_trg = blurred_h_src * fit_ratio;

      /*
        пикселизация фрагментов, на основе
        https://itnext.io/how-to-blur-objects-in-real-time-with-video-and-canvas-898cddc01ae6
      */
      /*const imgData = ctx && ctx.getImageData(
        0, 0,  this.video_canvas.width, this.video_canvas.height).data;
      let pixelSize = 4;

      for (let row = blurred_y_trg; row < blurred_y_trg + blurred_h_trg; row += pixelSize) {
        for (let col = blurred_x_trg; col < blurred_x_trg + blurred_w_trg; col += pixelSize) {
          let pixel = (col + ( row * this.video_canvas.width )) * 4;
          
          ctx.fillStyle = `rgba(${imgData[pixel]},${imgData[pixel + 1]},${imgData[pixel + 2]},${imgData[pixel + 3]})`;
          ctx.fillRect(col, row, pixelSize, pixelSize);
        }
      }*/

      this.fill_pixelate(
        [
          {x:300, y:300, w:200, h:200},
          {x:700, y:400, w:200, h:200}
        ],
            tmpCanvas, tmpContext);
      // !!! счётчик this.video.currentTime

      // console.log("*** tmp w h before blur", tmpCanvas.width, tmpCanvas.height);

      this.fill_blur(
        [
          {x:400, y:600,w:300, h:300},
          {x:700, y:800,w:300, h:300},
        ],
        this.video, tmpContext
        );

      console.log("*** tmp w h after blur", tmpCanvas.width, tmpCanvas.height);

      /* копирование временного canvas на отображаемый */
      var fit_ratio = Math.min( this.video_canvas.width / tmpCanvas.width,
        this.video_canvas.height / tmpCanvas.height); 
      var fit_width = this.video.videoWidth * fit_ratio;
      var fit_height = this.video.videoHeight * fit_ratio;

      var fit_x = (this.video_canvas.width - fit_width) / 2;
      var fit_y = (this.video_canvas.height - fit_height) / 2;
      
      ctx.filter = this.colorfilters;
      ctx.drawImage(tmpCanvas,
        0, 0,
        tmpCanvas.width, tmpCanvas.height,
        fit_x, fit_y,
        fit_width, fit_height);
    },

    resize_canvas()
    {
      console.log("***resize_canvas()");
      this.video_canvas.width = this.video.offsetWidth;
      this.video_canvas.height = this.video.offsetHeight;
    },

    fill_color(/* x, y, w, h, src_ctx, trg_ctx */){
      //
    },

    fill_blur(rects, src_ctx, trg_ctx){
      trg_ctx.filter = "blur(10px)";
      for (let i = 0; i < rects.length; i++) {
        trg_ctx.drawImage(src_ctx,
          rects[i].x, rects[i].y, rects[i].w, rects[i].h,
          rects[i].x, rects[i].y, rects[i].w, rects[i].h
        );
      }
      trg_ctx.filter = "none";
    }, 

    fill_pixelate( rects, trg_cnv,  trg_ctx) {
      /*
        пикселизация фрагментов, на основе
        https://itnext.io/how-to-blur-objects-in-real-time-with-video-and-canvas-898cddc01ae6
      */

      const imgData = trg_ctx
        && trg_ctx.getImageData(0, 0,  trg_cnv.width, trg_cnv.height).data;
      let pixelSize = 10;

      for (let i = 0; i < rects.length; i++) {
        for (let row = rects[i].y; row < rects[i].y + rects[i].h; row += pixelSize) {
          for (let col = rects[i].x; col < rects[i].x + rects[i].w; col += pixelSize) {
            let pixel = (col + ( row * trg_cnv.width )) * 4;
            trg_ctx.fillStyle =
              `rgba(${imgData[pixel]},${imgData[pixel + 1]},${imgData[pixel + 2]},${imgData[pixel + 3]})`;
            trg_ctx.fillRect(col, row, pixelSize, pixelSize);
          }
        }
      }
    },

    setup_color_filters() { // фильтры цвета
      /* на основе https://codepen.io/ygjack/pen/xrqQjR */
      this.colorfilters =
        `saturate(${this.saturate}) hue-rotate(${this.hue}deg) brightness(${this.brightness}) contrast(${this.contrast}) sepia(${this.sepia})`;
      console.log("***filters = ", this.colorfilters);
      this.drawImage();
    },

    startprocessing(video_object){ // запрос на начало обработки видео

      // при успешном запросе возвращается id обрабатываемой задачи
      axios.get("/api/startprocessing",
      { params: {id:video_object.id, type:this.backendFilters}})
      .then(response => {
        if(response.data.status!="ok"){
          this.pending_request_id = response.data.request_id;
        }
        else{
          this.pending_request_id = null;
        }
      })
      .catch(error => {
        this.pending_request_id = null;
        this.$emit("showerror","Ошибка сервера ", error);
      });
    },

    waitprocessing(/* video_object */){ // polling завешения обработки
      // при успешном запросе возвращается имя файла обработанного видео
      // (или процент выполнения и видео-заглушка)
      axios.get("/api/waitprocessing")
      .then(response => {
        if(response.data.status!="ok"){
          const poster_class = document.querySelector('.vjs-poster');
          poster_class.style.display = 'block';
          poster_class.style.backgroundImage = 'loading_screen.gif';
          this.player.posterImage.show();
          //$('.vjs-poster').css({
          //  'background-image': 'url('+videoposter+')',
          //  'display': 'block'
          //});
          
          this.percent_ready = response.data.percent_ready;
        }
        else{
          this.pending_request_id = null;
        }
      })
      .catch(error => {
        this.pending_request_id = null;
        this.videourl = "videostub.mp4";
        this.percent_ready = 100;
        this.$emit("showerror","Ошибка сервера ", error);
      });
    },

    show_wait_poster(){
      // const poster_class = document.querySelector('.vjs-poster');
      // console.log("*** poster_class = ", poster_class);
      // this.player.posterImage = "loading_screen.gif";
      // poster_class.display = 'block';
      // poster_class.backgroundImage = 'loading_screen.png';
      this.player.poster("loading_screen.gif");
      // this.player.poster(null);
    }
  },  

  watch:{
    saturate(){ this.setup_color_filters(); },
    brightness(){ this.setup_color_filters(); },
    hue(){ this.setup_color_filters(); },
    sepia(){ this.setup_color_filters(); },
    contrast(){ this.setup_color_filters(); },

    selectedVideo(nextValue /*, prevValue */){
      // console.log("prevValue = ", prevValue);
      // console.log("nextValue = ", this.videos[nextValue]);
      this.player.src(this.videos[nextValue].url);
    },

  },

  mounted(){
    
    this.video = document.getElementById("video-id");
    this.video_canvas = document.getElementById("video-canvas-id");
    /*
    this.fabric_canvas = new fabric.Canvas("video-canvas", {selection: false});
    //this.fabric_canvas.selection = false;
    */

    // var videoEl = document.getElementById('video');
    // var video1 = new fabric.Image(videoEl, {
    //   left: 0,
    //   top: 0
    // });
    // fabric_canvas.add(video1);


    // this.video.onplay = function() {
    //   clearInterval(this.canvasInterval);
    //   this.canvasInterval = window.setInterval(() => {
    //     this.drawImage();
    //   }, 1000 / 30);
    // };

    // this.test_circle = new fabric.Circle({
    //     left: 100,
    //     top: 100,
    //     originX: 'left',
    //     originY: 'top',
    //     radius: 100,
    //     angle: 0,
    //     fill: 'red',
    //     stroke: 'blue',
    //     strokeWidth: 5,
    // });
    // fabric_canvas.add(this.test_circle);

    this.player = videojs(this.video, this.options, () => {
      this.resize_canvas();

      this.player.log('onPlayerReady', this);
      this.resize_canvas();
      this.player.on(
      'play',
      () => {
        console.log("**callback");
        
        this.canvasInterval = window.setInterval(() => {
          this.drawImage();
        }, 1/30);
      });

      this.player.on('pause', () => {
        console.log("***onpause");
        clearInterval(this.canvasInterval);
      });

      this.player.on('ended', () => {
        console.log("***onended");
        clearInterval(this.canvasInterval);
      });

      this.player.on('seeked', () => {
        //this.resize_canvas();
        this.drawImage();
      });


    });

    // const poster_class = document.querySelector('.vjs-poster');
    // console.log();
    // poster_class.style.display = 'block';
    // poster_class.style.backgroundImage = 'loading_screen.png';
    // this.player.posterImage.show();

    // this.video.addEventListener(
    //   "play",
    //   () => {
    //     // this.width = video.videoWidth / 2;
    //     // this.height = video.videoHeight / 2;
    //     // this.timerCallback();
    //     this.resize_canvas();
    //     console.log("**callback");
    //   },
    //   false
    // );
    
    


    /* код для растяжения uppy dashboard на 100% по высоте*/
    document.getElementsByClassName("uppy-Dashboard")[0].style.height = '100%';
    const uppy_root = document.getElementsByClassName("uppy-Root")[0];
    // console.log("uppy_root= ", uppy_root);
    uppy_root.style.height = '100%';
    const uppy_outer_div = uppy_root.parentElement;
    // console.log("uppy_outer_div= ", uppy_outer_div);
    uppy_outer_div.style.height = '82%';
    // console.log("uppy_outer_div= ", uppy_outer_div);

  },

  beforeDestroy() {
    this.uppy.close({ reason: 'unmount' });

    if (this.player) {
      this.player.dispose();
    }
  },

}
</script>

<style>

.video-canvas-container {
  margin: 0 auto;
  width: 100%;
  height: 70%;
  position: relative;
}

.video { top:0; left:0;width: 100%; height: 100%; position: absolute;}
.canvas { top:0; left:0;position: absolute; z-index: 10;
  pointer-events:none; /* отменить перехват событий мыши канвасом */
}

.vjs-control-bar {
  display: block;
}

/* Always show control bar */
.vjs-control-bar {
  display:block;
}

/* Don't fade out controls */
.video-js.vjs-static-controls.vjs-has-started.vjs-user-inactive.vjs-playing .vjs-control-bar {
  opacity: 1;
  visibility: visible; 
}

/* Align poster to top */
.video-js.vjs-static-controls .vjs-poster {
  background-position: 50% 0;
}

/* Override tech height:100% */
.video-js.vjs-static-controls .vjs-tech {
  height: auto;
  height: calc(100% - 30px);
}

/* запрет кнопки fullscreen */
.vjs-nofull .vjs-fullscreen-control {
  display:none;
}

/* запрет кнопки fullscreen */
.vjs-nofull .vjs-picture-in-picture-control {
  display:none;
}
/*.swapvideo {
	width: 50%;
    float: left;
    padding-right: 5px;
}
.swapvideo .swaptitle {
	margin-bottom: 20px;
}
.swapvideo .overlayvideo {
    position: relative;
}
.canvas-container {
    position: absolute !important;
}
.swapvideo .overlayvideo .video-js {
    width: 100%;
}
.swaptitle h2 {
	text-align: center;
}
.swap_video_btn {
    width: 100%;
}
.swap_video_btn .playbtninner {
    width: auto;
    margin: 0;
}


.swap_video_btn .play_block_center {
    width: 100%;
    overflow: hidden;
    text-align: left;
    margin-top: 15px;
}

.toolblock {
    overflow: hidden;
    float: left;
}
.toolblock .inner_tool {
    width: 100%;
    overflow: hidden;
}
.toolblock .inner_tool button {
    width: 53px;
    height: 50px;
    line-height: 50px;
    background: #fff;
    border: 1px solid #cccccc;
        border-right-color: rgb(204, 204, 204);
        border-right-style: solid;
        border-right-width: 1px;
    border-right: none;
    float: left;
    padding: 0px;
}
.toolblock .inner_tool button:last-child {
     border-right: 1px solid #cccccc;
    }
.toolblock .inner_tool button.active {
    background: #E9E9E9;
}
.toolblock .inner_tool button .toolicon2 {
    background-position: -36px 0;
}
.toolblock .inner_tool button .toolicon3 {
    background-position: -72px 0;
}
.toolblock .inner_tool button .toolicon4 {
    background-position: -108px 0;
}

.bothplay .navbtn i {
    width: 22px;
    height: 17px;
}
.playblock .navbtn {
    width: 32px;
    height: 32px;
    top: 4px;
}
.playblock .navbtn {
    background: #00a6ff;
    width: 36px;
    height: 36px;
    position: relative;
    top: 2px;
}
.playblock button {
    border: none;
    padding: 0;
}
.playblock .playbtn {
    width: 120px;
    height: 37px;
    line-height: 37px;
    font-size: 15px;
}

.playbtninner .playblock .playbtn {    
    background: #00a6ff;
    width: 140px;
    height: 40px;
    line-height: 40px;
    color: #fff;
    font-size: 16px;
    font-family: 'ralewaybold';
}
.playbtninner .playblock .navbtn i {
    margin: 0 auto;
    width: 18px;
    height: 15px;
    display: block;
}
.playbtninner .playblock .navbtn i {
    width: 15px;
    height: 13px;
}
.video_palybtnblock{
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
}
.video_palybtnblock .zoombtn{
    margin: 10px 0;
}
.video_palybtnblock .zoombtn button{
    padding: 6px 20px;
    cursor: pointer;
} 
.video_palybtnblock .slowmotion h4{
    font-size: 16px;
    font-weight: 600;
}
.line-drawing-tools{
    font-size: 15px;
    color: #15b18a;
}

.slowmotionblock button{
    background-color: #f3f3f3;
    border:1px solid #ccc;
    padding: 7px 15px;
    cursor: pointer;
}
.slowmotionblock button.active{
    background-color: #c2c2c2;
}*/

</style>