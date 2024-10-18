<template>
    <div class="title-background"></div>
    <div class="centered-div center-vertically">
        <div class="title-text">Spielende!</div>
        <button class="title-play-button" @click="play">Zurück zum Start</button>
    </div>
    <RouterView />
</template>

<script>
    import { onMounted } from 'vue'
    import { RouterLink, RouterView } from 'vue-router'
    import { useRouter } from 'vue-router';
    import { useStore } from 'vuex';

    export default {
        setup() {
            const router = useRouter();

            onMounted(() => {
                
            });

            function play() {
                router.push('/title');
            }

            return {
                play
            }
        }
    }

</script>