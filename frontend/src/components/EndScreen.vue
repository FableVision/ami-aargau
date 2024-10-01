<template>
    <div class="title-background"></div>
    <div class="centered-div center-vertically">
        <div class="title-text">Game Name Here</div>
        <button class="title-play-button" @click="play">Play</button>
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