<script>
  import { createEventDispatcher } from 'svelte';

  export let showLogIn = false;
  const dispatch = createEventDispatcher();

  let username = '';
  let password = '';

  function logInHandler() {
    dispatch('login', { username, password });
    closeHandler(); // Optionally close the modal after dispatching
  }

  function closeHandler() {
    dispatch('closeModal');
  }
</script>

{#if showLogIn}
<div class="modal fixed inset-0 bg-black bg-opacity-50 z-50 flex justify-center items-center">
  <div role="dialog" aria-modal="true" class="bg-white p-6 rounded-md w-1/3 space-y-4">
    <h2 class="text-2xl font-bold">Log In</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div>
        <label for="username" class="block font-medium text-gray-700">Username</label>
        <input type="text" id="username" bind:value={username} placeholder="JohnSmith" class="w-full p-2 border rounded"/>
      </div>
      <div></div> <!-- This empty div can be removed if it's not serving any purpose -->
      <div>
        <label for="password" class="block font-medium text-gray-700">Password</label>
        <input type="password" id="password" bind:value={password} placeholder="••••••••" class="w-full p-2 border rounded" />
      </div>
    </div>
    <div class="flex justify-end space-x-2">
      <button class="bg-gray-300 hover:bg-gray-400 text-black font-bold py-2 px-4 rounded" on:click={closeHandler}>Cancel</button>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" on:click={logInHandler}>Log In</button>
    </div>
  </div>
</div>
{/if}
