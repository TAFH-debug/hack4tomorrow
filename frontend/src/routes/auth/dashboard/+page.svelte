<script>
    import Project from "../../components/project.svelte";
    import { goto } from '$app/navigation';

    export let data;

    function show() {
        var inp = document.getElementById("np_inp");
        inp.style.display = "flex";
    }

    function hide() {
        var inp = document.getElementById("np_inp");
        inp.style.display = "none";
    }

    function send() {
        var inp = document.getElementsByClassName("desc_input")[0];
        const description = inp.value;

        const token = btoa(data.username + ":" + data.password);
        document.getElementById("loading").style.display = "block";
        fetch("http://165.227.130.2:8000/project/generate_basic/", {
            method: "POST",
            headers: {
                Authorization: `Basic ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                project_description: description
            })
        }).then(
            (e) => {
                goto("/")
                document.getElementById("loading").style.display = "none";
            })
    }

    function f(e) {
        e.stopPropagation();
    }
</script>

<div class="outer" data-sveltekit-reload>
    <div id="np_inp" on:click={hide}>
        <div class="inp_d" on:click={f}>
            <div class="inp_t">Brief game description:</div>
            <input class="desc_input" description="description" />
            <input class="sbm" type="submit" value="Create" on:click={send}/>
        </div>
    </div>
    <div class="container">
        <span class="title">Projects</span>
        <div class="projects">
            {#each data.projects as project}
            <Project project={project} />
            {/each}
            <button class="create_project" on:click={show}>
                <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4 12H20M12 4V20" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
        </div>
    </div>
</div>


<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');

    .outer {
        width: 100vw;
    }

    #np_inp {
        top: 0;
        bottom: 0;
        width: 100vw;
        display: none;
        position: absolute;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .inp_d {
        display: flex;
        flex-direction: column;
        justify-content: center;
        background-color: white;
        border-radius: 20px;
        width: 20vw;
        height: 40vh;
    }

    .inp_t {
        margin: 10px;
        text-align: center;
        font-size: 20px;
    }

    .desc_input {
        outline: none;
        background-color: none;
        margin: 20px;
    }

    .sbm {
        background-color: rgb(80, 80, 196);
        border: none;
        border-radius: 5px;
        margin: 20px;
        padding: 10px;
        color: white;
    }

    .sbm:hover {
        background-color: rgb(106, 106, 195);
    }

    .container {
        width: 100vw;
        background-color: white;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .title {
        margin: 20px;
        color: black;
        font-family: Poppins, sans-serif;
        font-size: 30px;
        text-align: center;
    }

    .projects {
        display: flex;
        flex-wrap: wrap;
    }

    .create_project {
        border: none;
        height: 25vw;
        width: 20vw;
        border-radius: 10px;
        margin: 20px;
        padding: 20px;
        background-color: rgb(220, 220, 220);
        transition: all 0.5s;
        align-items: center;
        display: flex;
        cursor: pointer;
        justify-content: center;
    }

    .create_project:hover {
        background-color: rgb(195, 195, 195);
    }
</style>