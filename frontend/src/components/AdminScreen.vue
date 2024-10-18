<template>
    <div id="top-buttons-container">
        <button class="nav-button" id="home-button" @click="home">
            <img id="home-image" src="@/assets/png/home.png">
        </button>
    </div>
    <div id="choose-a-team" class="centered-div">
        <div class="game-main-text">Klicke auf ein Team, um die Antworten zurück zu setzen.</div>
        <div class="team-selection">
            <div class="team-container">
                <button class="team-img-container" @click="reset('ant')">
                    <img class="team-img" src="@/assets/png/ant.png">
                </button>
                {{Ant}}
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="reset('butterfly')">
                    <img class="team-img" src="@/assets/png/butterfly.png">
                </button>
                {{Butterfly}}
                
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="reset('cat')">
                    <img class="team-img" src="@/assets/png/cat.png">
                </button>
                {{Cat}}
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="reset('octopus')">
                    <img class="team-img" src="@/assets/png/octopus.png">
                </button>
                {{Octopus}}
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="reset('whale')">
                    <img class="team-img" src="@/assets/png/whale.png">
                </button>
                {{Whale}}
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="reset('owl')">
                    <img class="team-img" src="@/assets/png/owl.png">
                </button>
                {{Owl}}
            </div>
        </div>
        <div style="height: 50px"></div>
        <button class="confirm-button" @click='reset("ALL")'>Alle Teams zurücksetzen</button>
    </div>
    <RouterView />
  </template>

<script>
    import { onMounted } from 'vue'
    import { RouterLink, RouterView } from 'vue-router'
    import { useRouter } from 'vue-router';
    import { ref } from 'vue'
    import { useStore } from 'vuex';
    import allText from '@/text/text.json'

    export default {
        setup() {
            const router = useRouter();

            onMounted(() => {
                console.log("on mounted");
            });
            
            const Ant = ref('Ameise');
            const Butterfly = ref('Schmetterling');
            const Cat = ref('Katze');
            const Octopus = ref('Oktopus');
            const Owl = ref('Eule');
            const Whale = ref('Wal');
            
            function reset(groupname) {
                let resetMode = "FULLRESET";
                if(groupname == "ALL"){
                    resetMode = "FULLRESETALL";

                    Ant.value = "Ameise Reset!";
                    Butterfly.value = "Schmetterling Reset!";
                    Cat.value = "Katze Reset!";
                    Octopus.value = "Oktopus Reset!";
                    Owl.value = "Eule Reset!";
                    Whale.value = "Wal Reset!";
                }
                else{
                    if(groupname == "ant") Ant.value = "Ameise zurücksetzen";
                    if(groupname == "butterfly") Butterfly.value = "Schmetterling zurücksetzen";
                    if(groupname == "cat") Cat.value = "Katze zurücksetzen";
                    if(groupname == "octopus") Octopus.value = "Oktopus zurücksetzen";
                    if(groupname == "owl") Owl.value = "Eule zurücksetzen";
                    if(groupname == "whale") Whale.value = "Wal zurücksetzen";
                }

                const group = groupname;
                const question = 1;
                const answer = resetMode;
                
                const params = new URLSearchParams({
                    group: group,
                    question: question,
                    answer: answer
                });

                const baseUrl = import.meta.env.VITE_API_URL;
                console.log(baseUrl);
                fetch(baseUrl + '/receive?' + params.toString(), {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({message: ""}),
                })
                .then(response => response.json())
                .then(data => console.log(data));
            }

            function back(){

            }

            function home(){
                router.push('/title');
            }

            return {
                back, home, reset, Ant, Cat, Butterfly, Owl, Octopus, Whale
            }
        }
    }

</script>