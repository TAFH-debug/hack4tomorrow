<script>
    import { goto } from '$app/navigation';
    import Dialog from '../../../../components/dialog.svelte';

    export let data;

    function show() {
        var inp = document.getElementById("popup");
        inp.style.display = "flex";
    }

    function hide() {
        var inp = document.getElementById("popup");
        inp.style.display = "none";
    }

    function generate() {
        const token = btoa(data.username + ":" + data.password);
        const id1 = document.getElementById("popup_select1").value;
        const desc1 = document.getElementById("popup_input1").value;
        const id2 = document.getElementById("popup_select2").value;
        const desc2 = document.getElementById("popup_input2").value;

        document.getElementById("loading").style.display = "block";
        fetch("http://165.227.130.2:8000/dialog/create/", {
            
            method: "POST",
            headers: {
                Authorization: `Basic ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                project_id: parseInt(data.slug),
                character1_id: id1,
                character1_goal: desc1,
                character2_id: id2,
                character2_goal: desc2,
            })
        }).then(
            (e) => {
                goto("/auth/projects/" + data.slug)
                document.getElementById("loading").style.display = "none";
            })
    }

    function stopClick(e) {
        e.stopPropagation();
    }
</script>

<div class="outer">
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div id="popup" on:click={hide}>
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="popup_cont" on:click={stopClick}>
            <div class="popup_title">Character 1:</div>
            <select id="popup_select1" class="popup_select">
                {#each data.entities as item}
                <option value={item.id}>{item.name}</option>
                {/each}
            </select>
            <div class="popup_title">Character 1 goal:</div>
            <input class="popup_input" id="popup_input1" />
            <div class="popup_title">Character 2:</div>
            <select id="popup_select2" class="popup_select">
                {#each data.entities as item}
                <option value={item.id}>{item.name}</option>
                {/each}
            </select>
            <div class="popup_title">Character 2 goal:</div>
            <input class="popup_input" id="popup_input2" />
            <input class="sbm" type="submit" value="Create" on:click={generate}/>
        </div>
    </div>
    <div class="container">
        <span class="title">Dialogs</span>
        <div class="projects">
            {#each data.dialogs as dialog}
            <Dialog dialog={dialog} username={data.username} password={data.password} slug={data.slug}/>
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
        width: 80%;
        margin: 0 20px;
    }

    #popup {
        right: 0;
        left: 0;
        top: 0;
        bottom: 0;
        width: 100%;
        display: none;
        position: absolute;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: rgba(0, 0, 0, 0.3);
        font-family: Poppins, sans-serif;
    }

    .popup_cont {
        display: flex;
        flex-direction: column;
        justify-content: center;
        background-color: white;
        border-radius: 20px;
    }

    .popup_title {
        margin: 10px;
        margin-bottom: 0;
        text-align: center;
        font-size: 20px;
    }

    .popup_input {
        outline: none;
        background-color: none;
        margin: 20px;
        margin-top: 0;
    }

    .popup_select {
        outline: none;
        background-color: none;
        padding: 20px;
        margin: 10px;
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
        width: 100%;
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
        height: 25%;
        width: 20%;
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