<script>
    // We'll ensure the sparkles spawn within a safe zone, avoiding the edges
    const safeZoneOffset = 5; // Adjust this value to increase/decrease the safe zone

    let sparkles = Array.from({ length: 50 }, () => ({
        x: (Math.random() * (100 - 2 * safeZoneOffset)) + safeZoneOffset,
        y: (Math.random() * (100 - 2 * safeZoneOffset)) + safeZoneOffset,
        size: Math.random() * 2 + 1, // Sparkles will vary between 1px and 3px
        animationDuration: Math.random() * 3 + 2, // Animation duration between 2s and 5s
        animationDirection: Math.random() < 0.5 ? 'normal' : 'reverse' // Some sparkles will drift in reverse direction
    }));
</script>

<style>
    .sparkle {
        position: absolute;
        width: 1px;
        height: 1px;
        background-color: white;
        box-shadow: 0 0 2px 2px white;
        border-radius: 50%;
        animation-name: drift;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }

    @keyframes drift {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(10px, 15px) scale(1.5); }
    }
</style>

{#each sparkles as {x, y, size, animationDuration, animationDirection}}
    <div class="sparkle" style="
        left: {x}vw; 
        top: {y}vh; 
        width: {size}px; 
        height: {size}px; 
        animation-duration: {animationDuration}s;
        animation-direction: {animationDirection};
    "></div>
{/each}
