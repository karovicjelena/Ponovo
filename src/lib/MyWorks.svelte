<script>
    import { onMount, onDestroy } from 'svelte';
  
    let showMenu = false;
    let menu; // Reference to the menu element
    let button; // Reference to the hamburger button
  
    function toggleMenu(event) {
      event.stopPropagation(); // Prevent the click from reaching the window
      showMenu = !showMenu;
    }
  
    function handleClickOutside(event) {
      if (showMenu && !menu.contains(event.target) && !button.contains(event.target)) {
        showMenu = false;
      }
    }
  
    onMount(() => {
      window.addEventListener('click', handleClickOutside);
    });
  
    onDestroy(() => {
      window.removeEventListener('click', handleClickOutside);
    });
  </script>
  
  <div class="absolute top-5 left-5 p-3 bg-green-800 bg-opacity-70 rounded-lg shadow-lg z-5">
    <button class="flex flex-col justify-around h-6 w-6" bind:this={button} on:click={toggleMenu}>
      <div class="w-full h-0.5 bg-white"></div>
      <div class="w-full h-0.5 bg-white"></div>
      <div class="w-full h-0.5 bg-white"></div>
    </button>
    </div>

    <div class={`fixed top-0 ${showMenu ? 'left-0' : '-left-full'} h-full w-64 bg-white bg-opacity-80 shadow-md p-6 transition-all ease-in-out duration-300`} bind:this={menu}>
        <div class="absolute bg-yellow-600 w-full p-3 left-0 top-0">
          <p class="text-gray-800">My Works</p>
        </div>
        <!-- Introducing a spacer or padding at the top of the first link -->
        <div class="pt-16"> <!-- Adjust the padding value as needed -->
          <a href="/work/1" class="block py-2 border-b border-gray-200 text-gray-800">Work 1</a>
          <a href="/work/2" class="block py-2 border-b border-gray-200 text-gray-800">Work 2</a>
          <!-- More links as desired -->
        </div>
      </div>



  
  