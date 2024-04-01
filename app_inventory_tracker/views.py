from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import InventoryTracker
from .serializers import InventoryTrackerSerializer


class InventoryTrackerListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the InventoryTracker items for given requested user
        """
        todos = InventoryTracker.objects.all()
        serializer = InventoryTrackerSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the InventoryTracker with given InventoryTracker data
        """
        data = {
            "name": request.data.get("name"),
            "url": request.data.get("url"),
            "count": request.data.get("count"),
        }
        serializer = InventoryTrackerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryTrackerDetailListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, item_name):
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            return InventoryTracker.objects.get(name=item_name)
        except InventoryTracker.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, item_name, *args, **kwargs):
        """
        Retrieves the Todo with given todo_id
        """
        todo_instance = self.get_object(item_name)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = InventoryTrackerSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, item_name, *args, **kwargs):
        """
        Updates the todo item with given todo_id if exists
        """
        todo_instance = self.get_object(item_name)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": todo_instance.name,
            "url": todo_instance.url,
            "count": request.data.get("count"),
        }
        serializer = InventoryTrackerSerializer(
            instance=todo_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, item_name, *args, **kwargs):
        """
        Deletes the todo item with given todo_id if exists
        """
        todo_instance = self.get_object(item_name)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        todo_instance.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
