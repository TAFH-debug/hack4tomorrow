<script>
    import "$lib/fonts.css";
    export let content;
    export let title;
    export let id;
    export let inverse;

    let isVisible = false;

    import { onMount } from 'svelte';
    onMount(() => {
        const block = document.getElementById("block" + id);
        let vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
        var elemRect = block.getBoundingClientRect();
        
        if (vh >= elemRect.top + elemRect.height - 10) {
            isVisible = true;
        } else {
            isVisible = false;
        }

        window.addEventListener('scroll', _ => {
            var elemRect = block.getBoundingClientRect();
            if (vh >= elemRect.top + elemRect.height - 10) {
                isVisible = true;
            } else {
                isVisible = false;
            }
        });
    });
</script>

<div class={"block" + (isVisible ? " block_anim" : "")} id={"block" + id}>
    {#if !inverse}
    <div class="block_title">
        {title}
    </div>
    <div class="block_content">
        {content}
    </div>
    {:else}
    <div class="block_content">
        {content}
    </div>
    <div class="block_title">
        {title}
    </div>
    {/if}
</div>

<style>
    .block {
        height: 200px;
        width: 100vw;
        color: white;
        font-family: Outfit, sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 30px 0 0 0;
        transition: all 1s;
    }

    .block * {
        margin: 20px;
    }

    .block_content {
        width: 40vw;
        font-size: 20px;
        transform: translate(+100px);
        opacity: 0;
        transition: all 1s;
    }

    .block_title {
        width: 40vw;
        font-size: 60px;
        font-weight: bold;
        transform: translate(-100px);
        opacity: 0;
        transition: all 1s;
    }

    .block_anim * {
        transform: none;
        opacity: 1;
    }
</style>