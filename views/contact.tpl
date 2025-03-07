%rebase('base.tpl', title='Write to us')

<div class="grid">
    <div>
        <hgroup>
            <h1>Use form to contact site owner.</h1>
            <p>Information about privacy policy can be found at link below</p>
            <a href="/privacy-policy">Privacy Policy</a>
        </hgroup>
    </div>

    <div>
        <form action="/contact">
            <input type="email" placeholder="your_email@example.com" name="mail" autocomplete="email" required>
            <input type="text" placeholder="Karol" name="name" autocomplete="name" required>
            <input type="text" name="message" id="message" placeholder="my message to you is?" required>
            <input type="submit" value="Submit">
        </form>
    </div>
</div>
