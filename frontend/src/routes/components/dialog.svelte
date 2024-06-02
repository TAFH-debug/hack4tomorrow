<script>
    import { goto } from '$app/navigation';

    export let dialog;
    export let username;
    export let password;
    export let slug;

    function del(e) {
        e.preventDefault()
        const token = btoa(username + ":" + password);
        document.getElementById("loading").style.display = "block";
        fetch(
            "http://165.227.130.2:8000/dialog/delete",
            {
                
                method: "POST",
                headers: {
                    Authorization: `Basic ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: dialog.id
                })
            }
        ).then((e) => {
            goto("/auth/projects/" + slug)
            document.getElementById("loading").style.display = "none";
        })
    }
</script>

<a href={"/auth/projects/" + slug + "/dialogs/" + dialog.id} id={dialog.id} class="dialog">
    <div class="input_cont">
        <div class="dialog_param">Character 1:</div>
        <div>{dialog.character1}</div>
        <div class="dialog_param">Character 2:</div>
        <div>{dialog.character2}</div>
    </div>
    <button on:click={del}>Delete</button>
</a>

<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
    .dialog {
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
        height: 20vw;
        width: 15vw;
    }

    .dialog:hover {
        color: rgb(39, 39, 39);
        background-color: rgb(195, 195, 195);
    }

    .dialog_param {
        text-align: center;
        font-size: 15px;
    }

    .dialog button {
        background-color: rgb(80, 80, 196);
        border: none;
        border-radius: 5px;
        margin: 20px;
        padding: 10px;
        color: white;
    }

    .input_cont {
        margin: 10px;
    }
</style>