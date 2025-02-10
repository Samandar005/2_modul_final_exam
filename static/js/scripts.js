document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.querySelector("input[name='image']");
    const imagePreview = document.getElementById("imagePreview");
    const placeholderIcon = document.getElementById("placeholderIcon");

    fileInput.addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.classList.remove("hidden");
                if (placeholderIcon) {
                    placeholderIcon.classList.add("hidden");
                }
            };
            reader.readAsDataURL(file);
        } else {
            imagePreview.classList.add("hidden");
            if (placeholderIcon) {
                placeholderIcon.classList.remove("hidden");
            }
        }
    });
});

 <div class="mb-6">
        <div class="border-b">
            <nav class="flex space-x-8">
                <button id="teachers-tab" class="px-1 py-4 text-sm font-medium text-blue-600 border-b-2 border-blue-600">
                    Teachers
                </button>
                <button id="subjects-tab" class="px-1 py-4 text-sm font-medium text-gray-500 border-b-2 border-transparent hover:border-gray-300">
                    Subjects
                </button>
            </nav>
        </div>
    </div>

    <div id="teachers-section" class="bg-white rounded-lg shadow-sm">
        <div class="p-6 border-b">
            <div class="flex items-center justify-between">
                <h2 class="text-lg font-semibold">Teachers</h2>
                {% if user == department.author %}
                <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
                    <i class="bi bi-plus"></i>
                    <span class="ml-2"><a href="{% url 'teachers:create' %}">Add Teacher</a></span>
                </button>
                {% endif %}
            </div>
        </div>
        <div class="p-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {% for teacher in department.teachers.all %}
                <div class="flex items-center space-x-4 p-4 border rounded-lg">
                    <div class="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center overflow-hidden">
                        <img src="{{ teacher.image.url }}" alt="image" class="w-full h-full object-cover">
                    </div>
                    <div>
                        <h3 class="font-medium">{{ teacher.first_name }} {{ teacher.last_name }}</h3>
                        <p class="text-sm text-gray-500">{{ teacher.position }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>

    <div id="subjects-section" class="bg-white rounded-lg shadow-sm hidden">
        <div class="p-6">
            <h2 class="text-lg font-semibold">Subjects</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-4">
                {% for subject in department.subjects.all %}
                    <div class="p-4 border rounded-lg">
                        <h3 class="font-medium">{{ subject.name }}</h3>
                        <p class="text-sm text-gray-500">{{ subject.description }}</p>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
</div>