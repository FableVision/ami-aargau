<template>
    <div class="title-background"></div>
    <div class="centered-div center-vertically">
        <div class="title-text">Beyoncé im Aargauer Kunsthaus</div>
        <button class="title-play-button" @click="play">Spielen</button>
    </div>
    <RouterView />
</template>

<script>
    import { onMounted } from 'vue'
    import { RouterLink, RouterView } from 'vue-router'
    import { useRouter } from 'vue-router';
    import { useStore } from 'vuex';
    import allText from '../text/text.json'

    export default {
        setup() {
            const router = useRouter();

            onMounted(() => {
                
            });

            function play() {
                router.push('/game');
            }

            return {
                play
            }
        }
    }

</script>