function openRegisterModal() {
    document.getElementById('registerModal').style.display = 'flex';
}

function closeRegisterModal() {
    document.getElementById('registerModal').style.display = 'none';
}

function proceedToGoogleForm(url) {
    // Alert ONLY if the URL parameter is completely empty or missing
    if (!url || url.trim() === '' || url === '#') {
        alert("Registration link will be updated shortly.");
        return;
    }

    let targetUrl = url.trim();

    // Ensure the link starts with https://
    if (!targetUrl.startsWith('http://') && !targetUrl.startsWith('https://')) {
        targetUrl = 'https://' + targetUrl;
    }

    // Open the valid link in a new tab
    window.open(targetUrl, '_blank');

    if (typeof closeRegisterModal === 'function') {
        closeRegisterModal();
    }
}

window.onclick = function(e) {
    const modal = document.getElementById('registerModal');
    if (e.target === modal) {
        closeRegisterModal();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // Select all the event cards
    const eventCards = document.querySelectorAll('.event-click-card');

    eventCards.forEach(card => {
        card.addEventListener('click', function() {
            // 1. Remove the glow class from ALL boxes
            eventCards.forEach(c => c.classList.remove('active-glow'));
            
            // 2. Add the glow class ONLY to the box that was clicked
            this.classList.add('active-glow');
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("cyberParticleCanvas");
    const ctx = canvas.getContext("2d");

    let width, height;
    let particles = [];
    
    // Track mouse position for interactive connections
    const mouse = {
        x: null,
        y: null,
        radius: 150 // Connection distance around cursor
    };

    window.addEventListener("mousemove", (e) => {
        mouse.x = e.x;
        mouse.y = e.y;
    });

    window.addEventListener("mouseout", () => {
        mouse.x = null;
        mouse.y = null;
    });

    function initCanvas() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        
        // Generate particle nodes
        particles = [];
        const particleCount = Math.floor((width * height) / 10000); // Scale with screen size
        
        for (let i = 0; i < particleCount; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 1.2,
                vy: (Math.random() - 0.5) * 1.2,
                size: Math.random() * 2 + 1
            });
        }
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);

        // Update and draw particles
        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];

            p.x += p.vx;
            p.y += p.vy;

            // Bounce off edges
            if (p.x < 0 || p.x > width) p.vx *= -1;
            if (p.y < 0 || p.y > height) p.vy *= -1;

            // Draw particle dot
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = "#00f0ff";
            ctx.fill();

            // Connect nodes close to each other
            for (let j = i + 1; j < particles.length; j++) {
                let p2 = particles[j];
                let dist = Math.hypot(p.x - p2.x, p.y - p2.y);

                if (dist < 100) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = `rgba(0, 240, 255, ${1 - dist / 100})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }

            // Connect nodes to mouse cursor
            if (mouse.x !== null && mouse.y !== null) {
                let mDist = Math.hypot(p.x - mouse.x, p.y - mouse.y);
                if (mDist < mouse.radius) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = `rgba(0, 240, 255, ${1 - mDist / mouse.radius})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }

        requestAnimationFrame(animate);
    }

    window.addEventListener("resize", initCanvas);
    initCanvas();
    animate();
});

