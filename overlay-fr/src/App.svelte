<script lang="ts">
  import { onMount } from "svelte";

  const name = "JaessDev";

  // intervals in seconds
  const intervals = [3, 5, 10, 30];

  let offset = $state(0); // px offset for animation

  function randomInterval() {
    return intervals[Math.floor(Math.random() * intervals.length)] * 1000;
  }

  async function animateLoop() {
    while (true) {
      const waitTime = randomInterval();
      console.log(`Chose wait time of ${waitTime}`);

      // wait before animation
      await new Promise((r) => setTimeout(r, waitTime));

      // move right
      offset = 300;
      await new Promise((r) => setTimeout(r, 1200));

      // move left
      offset = -300;
      await new Promise((r) => setTimeout(r, 1200));

      // back to center
      offset = 0;
      await new Promise((r) => setTimeout(r, 1200));
    }
  }

  onMount(() => {
    animateLoop();
  });
</script>

<main class="w-screen h-screen bg-transparent">
  <nav
    class="fixed top-0 left-0 w-full
           bg-black/40 backdrop-blur-md
           shadow-lg shadow-black/30"
  >
    <div class="relative flex items-center justify-center py-3 overflow-hidden">
      <h1
        class="text-3xl font-bold text-green-400 tracking-wide
               transition-transform duration-[1200ms] ease-in-out
               drop-shadow-[0_0_8px_rgba(34,197,94,0.8)]"
        style="transform: translateX({offset}px);"
      >
        {name}
      </h1>
    </div>

    <!-- underline -->
    <div
      class="h-[2px] w-full
             bg-gradient-to-r
             from-transparent via-green-400 to-transparent"
    ></div>
  </nav>
</main>

<style>
  :root {
    background-color: transparent !important;
    margin: 0;
    padding: 0;
  }
</style>
