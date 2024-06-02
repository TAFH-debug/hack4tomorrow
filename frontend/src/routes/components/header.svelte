<script>
    import "$lib/fonts.css";
    import Button from "./glowing_button.svelte";
    import ProfileIcon from "./profile_icon.svelte";

    export let isRegistered;
</script>

<div class="filler header">
    <a class="header_logo" href="/">Ludus AI</a>
    {#if !isRegistered}
    <div class="header_link_container">
        <Button href="/login" text="Login"/>
        <Button href="/register" text="Register"/>
    </div>
    {:else}
    <div class="header_link_container">
        <Button href="/auth/dashboard" text="Dashboard"/>
        <ProfileIcon />
    </div>
    {/if}
</div>
<!-- <div class="filler"></div> -->

<style>
    .header_logo {
        font-family: Outfit, sans-serif;
        font-weight: bolder;
        font-size: 40px;
        text-decoration: none;
        color: white;
    }

    .header_link_container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .filler {
        height: 20vh;
        width: 100vw;
    }

    .header {
        z-index: 1;
        /* position: fixed; */
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .header * {
        margin: 20px;
    }
</style>