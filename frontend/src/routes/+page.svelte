<script>
  import Block from "./components/moving_block.svelte";

  export let data;
</script>

<svelte:head>
    <style>
        * {
            margin: 0;
            padding: 0;
        }
    </style>
</svelte:head>

<div class="container">
    <Block id="1" title="What is Ludus AI?" content="It's powerful tool to create game design."/>
    <Block inverse id="2" title="Creating characters." content="You can easily create characters that fit your game theme."/>
    <Block id="3" title="Assets, concept art's, etc." content="Multiple tools that help to fully think over the plot of the game."/>
</div>


<style>
    .container {
        width: 100vw;
        min-height: 100vh;
        margin: 0;
        padding: 0;
    }
</style>