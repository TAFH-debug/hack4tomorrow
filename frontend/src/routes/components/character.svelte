<script>
    import { goto } from '$app/navigation';

    export let character;
    export let username;
    export let password;
    export let slug;

    function save() {

        const token = btoa(username + ":" + password);
        fetch(
            "http://198.211.109.211:8000/character/change",
            {
                
                method: "POST",
                headers: {
                    Authorization: `Basic ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: character.id,
                    name: character.name,
                    appearance: character.appearance,
                    personality: character.personality
                })
            }
        )
    }

    function del() {
        const token = btoa(username + ":" + password);
        document.getElementById("loading").style.display = "block";
        fetch(
            "http://198.211.109.211:8000/character/delete",
            {
                
                method: "POST",
                headers: {
                    Authorization: `Basic ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: character.id
                })
            }
        ).then((e) => {
            goto("/auth/projects/" + slug)
            document.getElementById("loading").style.display = "none";
        })
    }
</script>

<div href={"/auth/characters/" + character.id} id={character.id} class="character">
    <!-- <img alt="" src={"http://198.211.109.211:8000/images/" + character.image} /> -->
    <div class="input_cont">
        <div class="character_param">Name:</div>
        <input id="name" bind:value={character.name} />
    </div>
    <div class="input_cont">
        <div class="character_param">Appearance:</div>
        <textarea id="appearance" bind:value={character.appearance} />
    </div>
    <div class="input_cont">
        <div class="character_param">Personality:</div>
        <textarea id="personality" bind:value={character.personality} />
    </div>
    <button on:click={save}>Save</button>
    <button on:click={del}>Delete</button>
</div>

<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
    .character {
        border: none;
        outline: none;
        font-family: Poppins, sans-serif;
        display: flex;
        flex-direction: column;
        justify-items: center;
        align-items: center;
        background-color: rgb(220, 220, 220);
        text-decoration: none;
        padding: 20px;
        margin: 15px;
        color: black;
        border-radius: 10px;
        transition: all 0.5s;
        height: 40vw;
        width: 30vw;
    }

    .character:hover {
        color: rgb(39, 39, 39);
        background-color: rgb(195, 195, 195);
    }

    .character_param {
        text-align: center;
        font-size: 15px;
    }

    .character img {
        width: 80%;
        height: 50%;
        margin: 10px;
    }

    .character button {
        background-color: rgb(80, 80, 196);
        border: none;
        border-radius: 5px;
        margin: 20px;
        padding: 10px;
        color: white;
    }

    .character input, .character textarea {
        outline: none;
        border: none;
        padding: 5px;
        border-radius: 10px;
    }

    .input_cont {
        margin: 10px;
    }
</style>