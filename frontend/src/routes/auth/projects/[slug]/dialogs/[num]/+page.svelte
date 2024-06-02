<script>
    export let data;
    import { goto } from '$app/navigation';
    function generate() {
        const token = btoa(data.username + ":" + data.password);
        document.getElementById("loading").style.display = "block";
        fetch(
            "http://165.227.130.2:8000/dialog/generate/",
            {
                
                method: "POST",
                headers: {
                    Authorization: `Basic ${token}`,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: parseInt(data.num)
                })
            }
        ).then(() => {
            document.getElementById("loading").style.display = "none";
            goto("/auth/projects/" + data.slug)
        })
    }
</script>

<div class="cont" data-sveltekit-reload>
    {#each data.messages as message}
    <div class="message">
        <div class="message_author">{message.author}</div>
        <div class="message_content">{message.content}</div>
    </div>
    {/each}
    {#if data.messages.length == 0}
    <button class="message_button" on:click={generate}>Generate by AI</button>
    {/if}
</div>

<style>
    .cont {
        width: 80%;
        display: flex;
        flex-direction: column;
        background-color: white;
        border-radius: 20px;
        margin: 0 20px;
    }

    .cont * {
        margin: 20px;
    }

    .message_author {
        font-weight: bold;
    }

    .message_button {
        border: none;
        border-radius: 20px;
        background-color: rgb(100, 100, 255);
        transition: all 0.4s;
    }

    .message_button:hover {

        background-color: rgb(157, 157, 255);
    }
</style>