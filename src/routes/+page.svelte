<script>
  import SignUpModal from '$lib/modals/SignUpModal.svelte';
  import LogInModal from '$lib/modals/LogInModal.svelte';
  import { goto } from '$app/navigation';
  import FairyDast from '../lib/FairyDast.svelte';

  let showSignUp = false;
  let showLogIn = false;

  // Navigates to the About page
  const handleClick = () => {
    goto('/about');
  };

  // Closes both the Sign Up and Log In modals
  function closeModal() {
    showSignUp = false;
    showLogIn = false;
  }

  // Opens the Log In modal and ensures the Sign Up modal is closed
  function handleOpenLogIn() {
    showSignUp = false;
    showLogIn = true;
  }

  // This function should be enhanced to handle the actual login logic
  function handleLoggedIn() {
    // Navigate to the main page upon successful login
    goto('/main'); // Adjust the route as per your app's routing setup
  }

  // Add a handler for the signup event from the SignUpModal
  async function handleSignUp(event) {
    const { firstName, lastName, username, email, password } = event.detail;
    // Implement the sign-up logic here, similar to handleLoggedIn
    // This might involve calling your backend API to register the user
    // For now, we'll just close the modal and log the event details
    console.log('Sign Up Details:', { firstName, lastName, username, email, password });
    closeModal();
    // Optionally, navigate to a welcome page or show a success message
  }
</script>

  
  
    <div class="absolute top-0 left-0 w-full h-full" style="background: url('fairy.png') no-repeat center center; background-size: cover;"></div>
  <!-- Left side - Fixed position with Title and Details -->
  <div class="fixed top-0 left-0 h-screen w-1/2 flex flex-col items-center justify-center z-10">
    <div class="text-center">
      <!-- Logo or Icon -->
      <img src="leaf1.png" alt="Logo" class="mb-4" width="100" height="100"/>
      <h1 class="text-6xl p-2 shadow-custom font-bold text-black leading-none hover:scale-110 transition-transform">Tranquility</h1>
      <!-- Tagline -->
      <p class="text-xl p-8 text-black mt-2">Your peaceful AI companion</p>

         <button class="bg-green-700 text-white font-bold py-2 px-4 rounded hover:bg-green-900 transition duration-300" on:click="{() => showSignUp = true}">Sign Up</button>
          <button class="bg-orange-400 text-white font-bold py-2 px-4 rounded hover:bg-orange-600 transition duration-300 mt-2" on:click="{() => showLogIn = true}">Log In</button>
          <button on:click={handleClick}>Let's write!</button>
        </div>
      </div>
  
  
    <!-- Right side - Scrollable About Section with white overlay -->
    <div class="absolute top-0 right-0 h-full w-1/2 overflow-auto p-6" style="background: rgba(255, 255, 255, 0.1);">
      <!-- Right side content container with margins -->
      <div class="mr-auto ml-16 max-w-4xl">
        <!-- First "paper" section -->
        <div class="paper-section">
          <h2 class="text-4xl font-sunrise mb-5">What is Tranquility?</h2>
          <p class="text-lg mb-6">
            Imagine a place where your thoughts can roam free, and an AI, let's call it your digital confidante, is there to listen. That's Tranquility for you - a digital journal with a twist of AI empathy.
        </p>
    </div>
    
    <!-- Second "paper" section -->
    <div class="paper-section">
        <h2 class="text-4xl font-sunrise mb-5">How it works?</h2>
        <p class="text-lg">
            It's simple. You talk, we listen. You type in your daily musings, your victories, your defeats, and our AI, equipped with virtual ears and a heart, provides a response. It's like having a chat with an old friend who's really good at nodding and giving you virtual pats on the back.
        </p>
    </div>
  
    <!-- Third "paper" section -->
    <div class="paper-section">
        <h2 class="text-4xl font-sunrise mb-4">A Friendly Heads-Up!</h2>
        <p class="text-lg">
            While Tranquility is a great listener and loves to chat about your day, it's important to remember that it's more of a digital journal than a digital psychologist. Our AI is designed to provide responses based on empathy and understanding, not professional mental health advice.
            Think of it as a diary that writes back. It's here to provide comfort and a space to reflect, but it's not a substitute for professional help. So, if your challenges feel heavier than a backpack filled with textbooks, we encourage seeking support from a qualified professional.
        </p>
    </div>
  </div>
  </div> 
    
  
  <FairyDast />
  <SignUpModal {showSignUp} on:closeModal={closeModal} on:openLogIn={handleOpenLogIn} />
  <LogInModal {showLogIn} on:closeModal={closeModal} on:loggedIn={handleLoggedIn} />
  
  <style>
    .paper-section {
      background: #ffffff; 
      padding: 1.5rem; 
      margin-bottom: 2rem; 
      border-radius: 1rem; 
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
      overflow: hidden; 
      opacity: 0.8;
    }
    button {
    /* Your button styling */
    padding: 10px 20px;
    background-color: #5cb85c;
    border: none;
    color: white;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  