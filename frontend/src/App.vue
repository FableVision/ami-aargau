<template>
  <RouterView />
</template>

<script>
    import { ref, reactive, onMounted } from 'vue';
    import assets from './res/assets';

    export default {
      setup() {
        let appDiv = reactive({});
        let appBody = reactive({});
        let resizeTimeout = ref(undefined);

        onMounted(() => {
          appDiv = document.getElementById('app');
          appBody = document.body;
          window.addEventListener("resize", onResize);
          onResize();
        });

        function onResize(event) {
          clearTimeout( resizeTimeout );
          resizeTimeout = setTimeout( doResize, 100 );
        }

        function doResize() {
          // clearTimeout( resizeTimeout );

          // let availableRatio = window.innerWidth / window.innerHeight;

          // const targetRatio = 1.7777;

          // const textSizeFactor = 64;

          // let appWidth = window.innerWidth;

          // let appHeight = window.innerHeight;

          // if( availableRatio < targetRatio ) {

          //     appHeight = Math.round( appWidth / targetRatio );

          // } else {

          //     appWidth = Math.round( appHeight * targetRatio );
              
          // }

          // let fontSize = Math.round( appWidth / textSizeFactor ); 
          // appDiv.style.width = appWidth + 'px';

          // appDiv.style.height = appHeight + 'px';

          // appBody.style.fontSize = fontSize + 'px';

          // let aspect = 9/16; // 16:9 ratio
          // let aspectInverse = 1 / aspect;
          // let width  = appDiv.clientWidth,
          // height = appDiv.parentElement.clientHeight;

          // if (width / height > aspectInverse) {
          //     fontSize *= (height * aspectInverse) / 1024;
          //     height = "100%";
          // } else {
          //     fontSize *= width / 1024;
          //     height = "initial";
          // }
        }

        return { appDiv, appBody, onResize, doResize }
      }
    }

</script>